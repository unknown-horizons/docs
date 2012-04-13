"""
Set up paths and stuff so we can import from horizons.
"""

import os
import sys

os.chdir(sys.argv[1])
sys.path.insert(0, '.')

from run_tests import mock_fife_and_gui
from run_uh import init_environment

mock_fife_and_gui()
init_environment()

import horizons.main
db = horizons.main._create_main_db()

# we also need to load entities to get access to the yaml data
from horizons.extscheduler import ExtScheduler
from horizons.entities import Entities
from horizons.ext.dummy import Dummy
ExtScheduler.create_instance(Dummy()) # sometimes needed by entities in subsequent calls
Entities.load_buildings(db, load_now=True)
Entities.load_units(load_now=True)
