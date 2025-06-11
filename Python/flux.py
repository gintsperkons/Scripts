import custom_script as cs
import env
import utils
import sys
import shutil
import globals
import parse_args





def defaultHandle():
  print("handle Defaults")


def handle_commands(parsed_args):  
  import premake
  import setup
  import make
  commandHandles = {
      "run": defaultHandle,
      "premake":premake.handlePremake,
      "build":defaultHandle,
      "clean":defaultHandle,
      "setup":setup.handleSetup,
      "custom":defaultHandle,
      "make:env":make.handleMake
  }

  if parsed_args.command in commandHandles:
    commandHandles[parsed_args.command]()


globals.args = sys.argv[1:]
globals.envs = env.load_env()
globals.parsed_args = parse_args.parse()

globals.functions = {}
globals.custom_script = cs.import_custom("flux.py")

handle_commands(globals.parsed_args)






if utils.fileExists(globals.envs['TEMP_DIR']):
  shutil.rmtree(globals.envs['TEMP_DIR'])