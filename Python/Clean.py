import sys
import os
import shutil
import Defines

def clean(fileEnding,folderNames):
    import os
    import shutil
    for root, dirs, files in os.walk(Defines.projectPath):
        for file in files:
            for extension in fileEnding:
                if file.endswith(extension):
                    os.remove(os.path.join(root, file))
                    print("Removed: " + os.path.join(root, file))
        for dir in dirs:
            if dir in folderNames:
                shutil.rmtree(os.path.join(root, dir))
                print("Removed: " + os.path.join(root, dir))

if __name__ ==  "__main__":
    print("This is the main function")
    fileEndings = []
    folderNames = []
    cleanType = None if len(sys.argv) < 2 else sys.argv[1]
    if cleanType  == None or cleanType == "gen" or cleanType == "all":
        if os.path.exists(Defines.compileDir):
            shutil.rmtree(Defines.compileDir)
    if cleanType == "gen" or cleanType == "all":
        fileEndings += [".pyc",".pyo",".sln",".vcxproj",".vcxproj.filters",".vcxproj.user",
                "Makefile",".code-workspace","CMakeCache.txt","cmake_install.cmake"]
        folderNames += ["__pycache__",".vs",".vscode"]
    if cleanType == "all":
        fileEndings += ["run.bat","run.sh","premake.bat","premake.sh",
                        "build.bat","build.sh","clean.bat","clean.sh"]

    clean(fileEndings,
            fileEndings)
