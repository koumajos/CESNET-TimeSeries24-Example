#!/bin/bash

DIRECTORY="cesnet-time-series-2023-2024/institution_subnets/agg_1_hour/"

for metric in 'n_flows' 'n_packets' 'n_bytes' 'sum_n_dest_asn' 'average_n_dest_asn' 'std_n_dest_asn' 'sum_n_dest_ports' 'average_n_dest_ports' 'std_n_dest_ports' 'sum_n_dest_ip' 'average_n_dest_ip' 'std_n_dest_ip' 'tcp_udp_ratio_packets' 'tcp_udp_ratio_bytes' 'dir_ratio_packets' 'dir_ratio_bytes' 'avg_duration' 'avg_ttl'
do
    for FILE in "$DIRECTORY"/*
    do
    if [ -f "$FILE" ]; then
        echo "-v metric='$metric',id_ip='$(basename $FILE)' sarima_retraining_institution_subnets.sh"
        qsub -v "metric='$metric',id_ip='$(basename "$FILE")'" sarima_retraining_institution_subnets.sh
    fi
    done
done
