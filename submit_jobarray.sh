#!/bin/bash -l
#
#SBATCH --job-name=dustpy_array
#SBATCH --mail-type=FAIL
#SBATCH --mail-user=######put-your-email-here######
# we start 6 jobs with array index 0 to 5, but only 4 run at once
# each job gets one CPU and 4G of memory. Not that each failed 
# job will send an email, you can also say END or ALL for the
# mail-type but this may lead to many emails. 
#SBATCH --array=0-5%4
#SBATCH --output=%A-%a.slurm.out
#SBATCH --ntasks=1
#SBATCH --mem=4G
#SBATCH --time=7-00:00:00
#SBATCH --partition=cluster

# possibly load your python environment here.
# I use pixi here for managing the environment.
# you might want to load your conda environment
# here and just do
# 
#     python jobarray.py run -n $SLURM_ARRAY_TASK_ID

echo "=================================================================="
echo "Starting job"
echo -n "It's now "
date 

# start the job, here the array index is passed to the call
pixi run python jobarray.py run -n $SLURM_ARRAY_TASK_ID

echo "Job completed"
echo -n "It's now "
date
