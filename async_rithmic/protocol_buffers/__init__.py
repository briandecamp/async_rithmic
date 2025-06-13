"""Protocol buffer message types."""

import importlib
import os
import sys

# Import all *_pb2 modules from the current directory
current_dir = os.path.dirname(__file__)
for module_name in [f[:-3] for f in os.listdir(current_dir) if f.endswith('_pb2.py')]:
    importlib.import_module(f'.{module_name}', package=__name__)
