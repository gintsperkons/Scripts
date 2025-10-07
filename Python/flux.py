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
    import build
    import run
    import clean
    import init

    commandHandles = {
        "run": run.handleRun,
        "run:build": run.handleRun,
        "premake": premake.handlePremake,
        "build": build.handleBuild,
        "setup": setup.handleSetup,
        "make:env": make.handleMake,
        "make:custom": make.handleMake,
        "clean": clean.handleClean,
        "clean:all": clean.handleClean,
        "clean:gen": clean.handleClean,
        "clean:build": clean.handleClean,
        "exec": cs.handle_custom,
        "init": init.handleInit,
    }

    if parsed_args.command in commandHandles:
        commandHandles[parsed_args.command]()


globals.args = sys.argv[1:]
globals.envs = env.load_env()
globals.parsed_args = parse_args.parse()

globals.functions = {}
globals.custom_script = cs.import_custom("flux.py")

handle_commands(globals.parsed_args)


if utils.fileExists(globals.envs["TEMP_DIR"]):
    shutil.rmtree(globals.envs["TEMP_DIR"])

