#!/usr/bin/env python
# coding: utf-8

import itertools
from pathlib import Path

import click
import dustpy


# function to run a model
@click.command()
@click.option('-n', default=0, help='select simulation number')
def run(n):
    """Run dustpy simulation of a simulation grid"""
    # make a simulation with those parameters
    sim = dustpy.Simulation()
    ##########
    #!TODO CHANGE THIS -- put your setup here
    sim.ini.gas.alpha = combinations[n][0]
    sim.ini.star.M = combinations[n][1] * dustpy.constants.M_sun
    ##########

    # make a output folder name, initialize, and run
    name = _get_name(n)
    sim.initialize()
    sim.writer.datadir = name
    sim.writer.overwrite = True
    sim.run()


# function to get the folder name of a simulation #
@click.command()
@click.option('-n', default=0, help='select simulation number')
def get_name(n=0):
    print(_get_name(n))

def _get_name(n=0):
    """determine a folder name for the simulations"""

    #####
    #!TODO CHANGE THIS TO YOUR PARAMETERS/NAME
    alpha = combinations[n][0]
    m = combinations[n][1]
    #####

    return f'data_alpha{alpha:.2g}--m{m:.2g}'.replace('.','_')


# function to check status of a simulation
@click.command()
@click.option('-n', default=-1, help='get folder name of a simulation number, -1 means all')
def check_status(n=-1):
    """determine a folder name for the simulations"""
    if n == -1:
        for i in range(len(combinations)):
            check_status_single(i)
    else:
        check_status_single(n)
        
def check_status_single(n):
    name = _get_name(n)
    reader = dustpy.hdf5writer()
    reader.datadir = name

    files = reader.read.listfiles()
    if len(files) == 0:
        print(f'{n} - {name}: no files')
    else:    
        file = Path(files[-1])
        #data = reader.read.output(str(file))
        print(f'{n:<4d} - {name}: output #{file.name[4:8]}')


# combine the commands into one command line program

@click.group()
def group():
    pass

group.add_command(get_name)
group.add_command(run)
group.add_command(check_status)

# we make a set of parameter combinations
###########
#!TODO CHANGE THIS
values = [
    [1e-3, 3e-3, 1e-2], # alpha
    [0.1, 0.5, 1.0] # mstar
    ]
###########

combinations = list(itertools.product(*values))

if __name__ == '__main__':
    group()
