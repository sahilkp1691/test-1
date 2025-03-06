import os
import sys

# src/__init__.py

# This is the __init__.py file for the SCO-project package.
# It can be used to initialize the package and import necessary modules.


# Add the src directory to the system path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import necessary modules
# from .module1 import Class1, function1
# from .module2 import Class2, function2

__version__ = "0.1.0"
__author__ = "Sahil Pansare"

# Initialize package-level variables or configurations if needed
# config = {
#     'setting1': 'value1',
#     'setting2': 'value2',
# }

# You can also define package-level functions or classes here
# def initialize():
#     pass
