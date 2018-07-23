#!/usr/bin/env python
#    ____                   __               _____ _         
#   / __ \____  ___  ____  / /   ____ _____ / ___/(_)___ ___ 
#  / / / / __ \/ _ \/ __ \/ /   / __ `/ __ \\__ \/ / __ `__ \
# / /_/ / /_/ /  __/ / / / /___/ /_/ / /_/ /__/ / / / / / / /
# \____/ .___/\___/_/ /_/_____/\__,_/ .___/____/_/_/ /_/ /_/ 
#     /_/                          /_/ 
#
# Copyright (C) 2018: Nick Martin
# Author: Nick Martin
# 
# This file is part of OpenLapSim.
#
# OpenLapSim is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# OpenLapSim is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with OpenLapSim.  If not, see <http://www.gnu.org/licenses/>
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from openlapsim import utilities
import argparse

def main():
    """This is the entry point to the OpenLapSim program if used via a command line."""
    print()
    utilities.logo()
    print()

    parser = argparse.ArgumentParser(prog='OpenLapSim', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-sim file',
                        help='this is the full path of the file describing how to run the sumulation',
                        default='examples/example_sim.json')

    run(parser.parse_args())

def run(args):

    print(args)


