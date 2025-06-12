import globals as g
import platform
import custom_script as cs

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


def buildLinux():
    import subprocess
    import utils

    subprocess.run(["make"], check=True)
