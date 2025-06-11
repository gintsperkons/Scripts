import os
import importlib.util
import globals

def import_custom(file_path):

  def import_if_exists(path, module_name="custom_setup"):
      if os.path.exists(path):
          spec = importlib.util.spec_from_file_location(module_name, path)
          module = importlib.util.module_from_spec(spec)
          spec.loader.exec_module(module)
          return module
      else:
          print(f"⚠️ File '{path}' does not exist.")
          return None

  # Try to import setup.py
  custom_setup_module = import_if_exists(file_path)

  if custom_setup_module:
    #   Set the global variables in the imported module
    setattr(custom_setup_module, "args", globals.args)
    setattr(custom_setup_module, "envs", globals.envs)

    for key, value in globals.functions.items():
      setattr(custom_setup_module, key, value)
  return custom_setup_module

def execute_custom(function_name):
   pass


# def execute_custom(custom_script,gobj):
#   if len(gobj["variables"]["ARGS"]) >= 2:
#     custom_function = gobj["variables"]["ARGS"][1]
#     if hasattr(custom_script, custom_function):
#       getattr(custom_script, custom_function)()
#   else:
#     print("Please specify a function name to execute.")