import globals as g
import os
import shutil

def removeBuildDir():
    import utils
    import os

    build_dir = g.envs["COMPILE_DIR"]
    if utils.dirExists(build_dir):
        for root, dirs, files in os.walk(build_dir, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.rmdir(build_dir)
        print(f"Removed build directory: {build_dir}")

def removeGeneratedFiles():
    import utils
    import os
    dirs = ["__pycache__"]
    files = ["Makefile"]
    file_extensions = [".pyc", ".pyo"]
    #Remove from project folder
    for root, dirs, files in os.walk(os.getcwd()):
    # Remove target directories
        for dir_name in dirs:
            if dir_name in dirs:
                dir_path = os.path.join(root, dir_name)
                shutil.rmtree(dir_path, ignore_errors=True)
                print(f"Removed directory: {dir_path}")

        # Remove target files
        for file_name in files:
            if file_name in files or any(file_name.endswith(ext) for ext in file_extensions):
                file_path = os.path.join(root, file_name)
                os.remove(file_path)
                print(f"Removed file: {file_path}")


def handleClean():
    import utils

    if g.parsed_args.command == "clean:all":
        removeBuildDir()
        removeGeneratedFiles()

    elif g.parsed_args.command == "clean:build":
        removeBuildDir()

    elif g.parsed_args.command == "clean:gen":
        removeGeneratedFiles()

    else: 
        
        removeBuildDir()
