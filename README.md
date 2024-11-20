# README

This repo contains:

- a slurm script to run a job array using pixi,
- a script to run the setups
- a pixi file that defines the python environment

The setup contains a function to create the output file name, and to setup/run a dustpy simulation. Change those to your liking. The input number (i.e. the job array number) is used to select a parameter set from a list of parameter sets.


## Usage

Once you adapted `jobarray.py` for your setup, you can just submit the job with `sbatch submit_jobarray.sh`. If you were to call it directly, to run jobs, you would do

    python jobarray.py run -n 0

to run parameter set #0. To check all jobs you can use

    python jobarray.py check-status

## Pixi

The pixi.toml file defines an environment. The first time you use it, it will install it in that folder. It takes about 2 minutes and will add around 600 MB to the folder. You can trigger the installation with

    pixi install

or clean up afterwards with

    pixi clean

if you need more, you can add packages with

    pixi add mypackage

or for PyPI packages with

    pixi add --pypi mypackage


if needed you can "activate" the environment with `pixi shell`, for example to install it as a jupyter kernel

    python -m ipykernel install --user --name Pixi
