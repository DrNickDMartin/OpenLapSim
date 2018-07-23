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
# This file is part of openLapSim.
#
# openLapSim is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# openLapSim is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with openLapSim.  If not, see <http://www.gnu.org/licenses/>
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from openlapsim import __version__


def logo():
    """Print the OpenLapSim logo, version and copywrite informaiton"""

    logo = r""" https://drnickdmartin.github.io/OpenLapSim/
   ____                   __               _____ _         
  / __ \____  ___  ____  / /   ____ _____ / ___/(_)___ ___ 
 / / / / __ \/ _ \/ __ \/ /   / __ `/ __ \\__ \/ / __ `__ \
/ /_/ / /_/ /  __/ / / / /___/ /_/ / /_/ /__/ / / / / / / /
\____/ .___/\___/_/ /_/_____/\__,_/ .___/____/_/_/ /_/ /_/ 
    /_/                          /_/                       
    v""" + __version__.__version__

    print(logo)