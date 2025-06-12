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
    dirs_to_delete = ["__pycache__"]
    files_to_delete = ["Makefile"]
    file_extensions_to_delete = [".pyc", ".pyo"]
    #Remove from project folder
    for root, dirs, files in os.walk(os.getcwd()):
    # Remove target directories
        for dir_name in dirs_to_delete:
            dir_path = os.path.join(root, dir_name)
            if utils.dirExists(dir_path):
                shutil.rmtree(dir_path)
                print(f"Removed directory: {dir_path}")

        # Remove target files
        for file_name in files:
            if file_name in files_to_delete or any(file_name.endswith(ext) for ext in file_extensions_to_delete):
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
