# README

This repo contains:

- `submit_jobarray.sh`: a slurm script to run a job array using pixi,
- `jobarray.py`: a script to run the setups
- `pixi.toml`: a pixi file that defines the python environment

The script `jobarray.py` contains a function to define the output folder name for each run, and a function to setup+run a dustpy simulation. Change those functions and the list of parameters to your liking. The input number (i.e. the job array number) is used to select a parameter set from a list of parameter sets, which are also defined in that file.

Also adapt the `submit_jobarray.sh` to example run more simulations at a time (now its 4 at most) and to adjust the range of simulation numbers. 

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

if you need additional packages, you can add packages with

    pixi add mypackage

or for PyPI packages with

    pixi add --pypi mypackage

If needed you can "activate" the environment with `pixi shell`, for example to install it as a jupyter kernel

    python -m ipykernel install --user --name Pixi

If you need locally installed packages (e.g. something you cloned and installed with `pip install -e .`), you can put this into `pixi.toml` under the pypi section:

    [pypi-dependencies]
    idefixhelper = { path = "../CODES/idefixhelper", editable = true}

