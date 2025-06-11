import argparse
import globals



    


    
def parse():
    globals.config = {}
    parser = argparse.ArgumentParser(prog="flux", description="A lightweight project runner",
)
    subparsers = parser.add_subparsers(dest="command",metavar="Commands:")

    # run command
    # run_parser = subparsers.add_parser("run", help="launch the program")
    # run_parser.add_argument("-c","--conf")

    # premake_parser = subparsers.add_parser("premake", help="run premake")
    # premake_parser.add_argument('premake_args', nargs=argparse.REMAINDER, help="Args for premake5")

    # setup_parser = subparsers.add_parser("setup",help="setup project enviroment")

    make_env_parser = subparsers.add_parser("make:env",help="initialize .env file")

    return parser.parse_args()