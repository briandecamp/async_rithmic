"""Protocol buffer message types."""

import importlib
import os
import sys

# Add the generated directory to the Python path
generated_dir = os.path.join(os.path.dirname(__file__), 'generated')
if generated_dir not in sys.path:
    sys.path.insert(0, generated_dir)

# Import all *_pb2 modules from the generated directory
for module_name in [f[:-3] for f in os.listdir(generated_dir) if f.endswith('_pb2.py')]:
    importlib.import_module(f'.{module_name}', package=__name__)
