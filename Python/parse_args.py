import argparse
import globals


def parse():
    globals.config = {}
    parser = argparse.ArgumentParser(
        prog="flux",
        description="A lightweight project runner",
    )
    subparsers = parser.add_subparsers(dest="command", metavar="Commands:")

    clean_parser = subparsers.add_parser("clean", help="clean project files")
    clean_parser_all = subparsers.add_parser(
        "clean:all", help="clean all project files"
    )
    clean_parser_gen = subparsers.add_parser("clean:gen", help="clean generated files")
    clean_parser_build = subparsers.add_parser("clean:build", help="clean build files")

    build_parser = subparsers.add_parser("build", help="build the project")

    exec_parser = subparsers.add_parser("exec", help="execute a custom script")
    exec_parser.add_argument(
        "function", nargs="?", default=None, help="Name of the custom script to execute"
    )

    run_parser = subparsers.add_parser("run", help="launch the program")
    
    run_build_parser = subparsers.add_parser("run:build", help="rebuild and launch the program")

    premake_parser = subparsers.add_parser("premake", help="run premake")
    premake_parser.add_argument(
        "premake_args", nargs=argparse.REMAINDER, help="Args for premake5"
    )

    setup_parser = subparsers.add_parser("setup", help="setup project enviroment")

    make_env_parser = subparsers.add_parser("make:env", help="initialize .env file")
    
    init_parser = subparsers.add_parser("init", help="initialize a new flux project")

    return parser.parse_args()

