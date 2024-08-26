#!/usr/bin/python3
import os
import argparse
from argparse import RawTextHelpFormatter
import pandas as pd
import numpy as np

from statsmodels.tsa.statespace.sarimax import SARIMAX

import warnings

warnings.filterwarnings("ignore")


def parse_arguments() -> argparse.Namespace:
    """
    The `parse_arguments` function is used to parse command line arguments and return the parsed
    arguments.
    :return: The function `parse_arguments` returns the parsed command-line arguments as an
    `argparse.Namespace` object.
    """
    parser = argparse.ArgumentParser(
        description="""

    Usage:""",
        formatter_class=RawTextHelpFormatter,
    )
    parser.add_argument(
        "-p",
        help="",
        type=int,
        metavar="NUMBER",
    )
    parser.add_argument(
        "-d",
        help="",
        type=int,
        metavar="NUMBER",
    )
    parser.add_argument(
        "-q",
        help="",
        type=int,
        metavar="NUMBER",
    )
    parser.add_argument(
        "-P",
        help="",
        type=int,
        metavar="NUMBER",
    )
    parser.add_argument(
        "-D",
        help="",
        type=int,
        metavar="NUMBER",
    )
    parser.add_argument(
        "-Q",
        help="",
        type=int,
        metavar="NUMBER",
    )
    parser.add_argument(
        "-M",
        help="",
        type=int,
        metavar="NUMBER",
    )
    parser.add_argument(
        "-t",
        help="",
        type=int,
        metavar="NUMBER",
    )
    parser.add_argument(
        "-T",
        help="",
        type=int,
        metavar="NUMBER",
    )
    parser.add_argument(
        "--dataset",
        help="",
        type=str,
        metavar="STRING",
    )
    parser.add_argument(
        "--aggregation",
        help="",
        type=str,
        metavar="STRING",
    )
    parser.add_argument(
        "--metric",
        help="",
        type=str,
        metavar="STRING",
    )
    parser.add_argument(
        "--id_ip",
        help="",
        type=str,
        metavar="STRING",
    )
    return parser.parse_args()


def fill_missing(train_df, train_time_ids):
    df_missing = pd.DataFrame(columns=train_df.columns)
    df_missing.id_time = train_time_ids[~train_time_ids.isin(train_df.id_time)].values

    for column in train_df.columns:
        if column == "id_time":
            continue
        if column in [
            "tcp_udp_ratio_packets",
            "tcp_udp_ratio_bytes",
            "dir_ratio_packets",
            "dir_ratio_bytes",
        ]:
            df_missing[column] = 0.5
        else:
            df_missing[column] = 0  # train_df[column].mean()

    return (
        pd.concat([train_df, df_missing])
        .sort_values(by="id_time")
        .reset_index()[train_df.columns]
    )


def main():
    arg = parse_arguments()

    PATH = f"cesnet-time-series-2023-2024/{arg.dataset}/{arg.aggregation}/"
    SAVE_PATH = f"results/{arg.dataset}/{arg.aggregation}/"

    if arg.aggregation == "agg_10_minutes":
        PATH_TIMES = "cesnet-time-series-2023-2024/times/times_10_minutes.csv"
    elif arg.aggregation == "agg_1_hour":
        PATH_TIMES = "cesnet-time-series-2023-2024/times/times_1_hour.csv"
    elif arg.aggregation == "agg_1_day":
        PATH_TIMES = "cesnet-time-series-2023-2024/times/times_1_day.csv"
    else:
        return

    ORDER = (arg.p, arg.d, arg.q)
    SEASONAL_ORDER = (arg.P, arg.D, arg.Q, arg.M)

    TRAINING_PERIOD = arg.t
    TESTING_PERIOD = arg.T

    TS_METRIC = arg.metric

    df_times = pd.read_csv(f"{PATH_TIMES}")
    df_times["time"] = pd.to_datetime(df_times["time"])

    df = pd.read_csv(f"{PATH}{arg.id_ip}")
    df = df[["id_time", TS_METRIC]]
    df = fill_missing(df, df_times.id_time)
    df["time"] = df_times["time"]

    # Create Dict for predictions
    predictions = {
        "time": df["time"].to_list(),
        f"{TS_METRIC}": df[TS_METRIC].to_list(),
        f"{TS_METRIC}_predictions": [np.nan] * TRAINING_PERIOD,
    }

    # Run ARIMA with default setting
    tmp_index = 0
    while tmp_index <= df.id_time.max() - TRAINING_PERIOD:
        train_df = df[df.id_time < tmp_index + TRAINING_PERIOD]
        train_df = train_df[train_df.id_time >= tmp_index]
        train_data = train_df[TS_METRIC].to_numpy()

        model = SARIMAX(train_data, order=ORDER, seasonal_order=SEASONAL_ORDER)
        results = model.fit(disp=False)

        predictions[f"{TS_METRIC}_predictions"] += list(
            results.forecast(steps=TESTING_PERIOD)
        )
        tmp_index += TESTING_PERIOD

    if len(predictions[f"{TS_METRIC}_predictions"]) > len(predictions["time"]):
        predictions[f"{TS_METRIC}_predictions"] = predictions[
            f"{TS_METRIC}_predictions"
        ][: len(predictions["time"])]

    predictions_df = pd.DataFrame(predictions)
    predictions_df.to_csv(
        f"{SAVE_PATH}{arg.id_ip}{arg.metric}_({arg.t}_{arg.T})_({arg.p}_{arg.d}_{arg.q})_({arg.P}_{arg.D}_{arg.Q}_{arg.M}).csv",
        index=False,
    )


if __name__ == "__main__":
    main()
