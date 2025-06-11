import globals as g
import utils

def handleEnvMake():
    if utils.fileExists("Scripts/.env_default"):
        utils.copyFile("Scripts/.env_default",".env")
        print("Copied Default env data")

def handleMake():
    if g.parsed_args.command == "make:env":
        handleEnvMake()
    