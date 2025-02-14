import importlib

def reload_module(module_name):
    try:
        module = importlib.import_module(module_name)
        importlib.reload(module)
        print(f"Module '{module_name}' reloaded successfully.")
    except ModuleNotFoundError:
        print(f"Module '{module_name}' not found!")
    except Exception as e:
        print(f"An error occurred while reloading the module: {e}")

# Example usage
reload_module('your_module_name')