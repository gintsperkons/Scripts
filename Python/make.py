import globals as g
import utils

def handleEnvMake():
    if utils.fileExists("Flux/.env_default"):
        if utils.fileExists(".env"):
            print("Env file already exists")
            return
        utils.copyFile("Flux/.env_default",".env")
        print("Copied Default env data")

def handleCustomMake():
    if utils.fileExists("Flux/custom_default_py"):
        if utils.fileExists("flux.py"):
            print("Custom file already exists")
            return
        utils.copyFile("Flux/custom_default_py","flux.py")
        print("Copied Default custom script data")
    

def handleMake():
    if g.parsed_args.command == "make:env":
        handleEnvMake()
    if g.parsed_args.command == "make:custom":
        handleCustomMake()