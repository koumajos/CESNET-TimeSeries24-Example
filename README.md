# Example of usage of the CESNET-TimeSeries24 dataset

## Download the dataset

The CESNET-TimeSeries24 dataset is available in Zenodo platform <https://zenodo.org/record/13382427>

## View Example

[Example Jupyter Notebook](https://github.com/koumajos/CESNET-TimeSeries24-Example/blob/main/example.ipynb)

## Dataset processing

As example of processing of three dataset parts, we prepare the [SARIMA retraining Python module](https://github.com/koumajos/CESNET-TimeSeries24-Example/blob/main/sarima_retraining.py) with [BASH scripts](https://github.com/koumajos/CESNET-TimeSeries24-Example/tree/main/metacentrum_scripts/) which process all time series in datasets parts using qsub (prepared for running on metacentrum servers).

## Evaluation example

The example of evalution of SARIMA model is available in file [analyze-results.ipynb](https://github.com/koumajos/CESNET-TimeSeries24-Example/blob/main/analyze-results.ipynb)

## Cite as

Koumar, J., Hynek, K., Čejka, T. et al. CESNET-TimeSeries24: Time Series Dataset for Network Traffic Anomaly Detection and Forecasting. Sci Data 12, 338 (2025). https://doi.org/10.1038/s41597-025-04603-x

```
@Article{cesnettimeseries24,
    author={Koumar, Josef and Hynek, Karel and {\v{C}}ejka, Tom{\'a}{\v{s}} and {\v{S}}i{\v{s}}ka, Pavel},
    title={CESNET-TimeSeries24: Time Series Dataset for Network Traffic Anomaly Detection and Forecasting},
    journal={Scientific Data},
    year={2025},
    month={Feb},
    day={26},
    volume={12},
    number={1},
    pages={338},
    issn={2052-4463},
    doi={10.1038/s41597-025-04603-x},
    url={https://doi.org/10.1038/s41597-025-04603-x}
}
```

Josef Koumar, Karel Hynek, Pavel Šiška & Tomáš Čejka. (2024). CESNET-TimeSeries24: Time Series Dataset for Network Traffic Anomaly Detection and Forecasting [Data set]. Zenodo. <https://doi.org/10.5281/zenodo.13382427>

```
@dataset{koumar_2024_13382427,
  author       = {Koumar, Josef and
                  Hynek, Karel and
                  Čejka, Tomáš and
                  Šiška, Pavel},
  title        = {{CESNET-TimeSeries24: Time Series Dataset for 
                   Network Traffic Anomaly Detection and Forecasting}},
  month        = aug,
  year         = 2024,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.13382427},
  url          = {https://doi.org/10.5281/zenodo.13382427}
}
```
