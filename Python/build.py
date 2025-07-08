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
    # Check if bear is installed
    if shutil.which("bear"):
        print("🐻 Bear is installed, using: bear -- make")
        subprocess.run(["bear", "--", "make"], check=True)
    else:
        print("🔧 Bear not found, using plain make")
        subprocess.run(["make"], check=True)


def buildLinux():
    import subprocess
    import utils
    run_make_with_bear()
    # subprocess.run(["make"], check=True)
