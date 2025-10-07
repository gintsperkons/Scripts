from make import handleEnvMake
from globals import envs



def handleInit():
    import os
    import utils
    handleEnvMake()
    os.makedirs("Source", exist_ok=True)
    if not utils.fileExists("Source/main.cpp"):
        utils.copyFile("Flux/defaults/main.cpp", "Source/main.cpp")
        print("Created Source/main.cpp")
    if not utils.fileExists("premake5.lua"):
        utils.copyFile("Flux/defaults/premake5.lua", "premake5.lua")
        print("Created premake5.lua")
    if not utils.fileExists(".gitignore"):
        utils.copyFile("Flux/defaults/gitignore", ".gitignore")
        print("Created .gitignore")
    if not utils.fileExists("flux.sh"):
        utils.copyFile("Flux/defaults/flux.sh", "flux.sh")
        system_command = f"chmod +x flux.sh"
        os.system(system_command)
        print("Created flux.sh")
    if not utils.fileExists("flux.ps1"):
        utils.copyFile("Flux/defaults/flux.ps1", "flux.ps1")
        print("Created flux.ps1")
    if not utils.fileExists("README.md"):
        with open("README.md", "w") as f:
            f.write("# New Flux Project\nThis is a new Flux project.")
        print("Created README.md")
    if not utils.fileExists("flux.py"):
        utils.copyFile("Flux/defaults/custom_default_py", "flux.py")
        print("Created flux.py")
    print("Initialized new flux project")