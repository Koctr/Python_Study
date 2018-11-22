# -*- encoding:utf-8 -*-
# Author: Koctr


import os
import sys
from core import main


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(BASE_DIR)

main.run()
