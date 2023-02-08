# This file is part of the pywin32 package.

"""
setup.py for pywin32
"""

import sys
import os
import glob
import shutil
import re
import subprocess
from distutils.core import setup, Extension
from distutils.command.build_ext import build_ext
from distutils.command.build import build

# The version number is stored in the pywintypes module.
