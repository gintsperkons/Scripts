import globals as g
import platform
import custom_script as cs
import shutil
import subprocess

def handleBuild():
    cs.execute_custom_internal("beforeBuild")
    if platform.system().lower() == "windows":
        print("Building for Windows is not supported yet.")
    elif platform.system().lower() == "linux":
        buildLinux()
    elif platform.system().lower() == "darwin":
        print("Building for macOS is not supported yet.")
    else:
        print(f"Building for {platform.system()} is not supported yet.")
    cs.execute_custom_internal("afterBuild")



def run_make_with_bear():

    try:
        import os
        if not os.path.exists("Makefile"):
            subprocess.run(["python3", "Flux/Python/flux.py", "premake"], check=True)
        # Check if bear is installed
        subprocess.run(["make"], check=True)
    except subprocess.CalledProcessError as e:
        print(e)

def buildLinux():
    run_make_with_bear()
