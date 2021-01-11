"""
Copyright 2021 Andrey Plugin (9keepa@gmail.com)
Licensed under the Apache License v2.0
http://www.apache.org/licenses/LICENSE-2.0
"""

import os

BASE_DIR = os.getenv("BASE_DIR", os.getcwd())
PRODUCTION_WORK = os.getenv("EXTERNAL_WORK", False)
DATA_DIR = os.getenv("DATA", False)
REMOTE_SERVER = os.getenv("REMOTE_SERVER", "*")