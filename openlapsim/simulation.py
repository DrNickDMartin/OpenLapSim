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

class Simulation(object):
    """This class represents a simulation"""
    
    def __init__(self, name, setup, trajectory):
        self.name = name
        self.setup = setup
        self.tajectory = trajectory
        
    def run(self):
        print("Running simulation...")