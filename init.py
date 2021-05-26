#!/usr/bin/env python3

"""
Set up paths and stuff so we can import from horizons.
"""

import os
import sys

if len(sys.argv) > 1:
	uh_dir = sys.argv[1]
else:
	uh_dir = '../unknown-horizons'
os.chdir(uh_dir)
sys.path.insert(0, '.')

#from run_tests import mock_fife
from run_uh import init_environment

#mock_fife()
init_environment(True)

import horizons.main
db = horizons.main._create_main_db()

# we also need to load entities to get access to the yaml data
from horizons.extscheduler import ExtScheduler
from horizons.entities import Entities
from unittest.mock import Mock
ExtScheduler.create_instance(Mock()) # sometimes needed by entities in subsequent calls
Entities.load_buildings(db, load_now=True)
Entities.load_units(load_now=True)
