# What is reload() in Python?
# reload() is a function in the importlib module that allows you to reload a previously imported module without restarting the Python interpreter. 
# This is useful when modifying a module and wanting to apply the changes without exiting the program.

# Example of using reload()

import config  # First import
import importlib

# Print initial value from config.py
print(config.settings)  # Output: debug mode

# --- Modify config.py (change settings to "Production Mode") ---

# Reload the module to reflect changes
importlib.reload(config)

# Print updated value
print(config.settings)  # Output: Production Mode