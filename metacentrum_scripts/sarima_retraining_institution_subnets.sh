#!/bin/bash
#PBS -N RunJob
#PBS -l select=1:ncpus=1:mem=32gb
#PBS -l walltime=24:00:00

echo ${PBS_O_LOGNAME:?This script must be run under PBS scheduling system, execute: qsub $0}

# Load venv
HOMEDIR=/home/$USER
SYNCED=$HOMEDIR/synced
HOSTNAME=`hostname -f`
source $SYNCED/venv/bin/activate

EXECMAIL=`which mail`
$EXECMAIL -s "[JP-METACENTRUM-JOB] Processing day job 'sarima_retraining' is running on $HOSTNAME" $PBS_O_LOGNAME << EOFmail
The 'sarima_retraining' processing has started with parameters:
Using Python $(which python).
Host domain $HOSTNAME
EOFmail

cd $SYNCED

python ./sarima_retraining.py -p 1 -d 1 -q 1 -P 1 -D 1 -Q 1 -M 168 -t 744 -T 168 --dataset="institution_subnets" --aggregation="agg_1_hour" --metric="$metric" --id_ip="$id_ip"

EXECMAIL=`which mail`
$EXECMAIL -s "[JP-METACENTRUM-JOB] Processing day job 'sarima_retraining' is ended running on $HOSTNAME" $PBS_O_LOGNAME << EOFmail
The 'sarima_retraining' processing has ended.
Using Python $(which python).
Host domain $HOSTNAME
EOFmail
