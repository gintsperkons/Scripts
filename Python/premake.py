import globals as g
import utils
import subprocess
import platform

premakeFileName = "premake5"
osExecExtension = (
    ".exe" if platform.system().lower() == "windows" else
    "" if platform.system().lower() == "linux" else
    "" if platform.system().lower() == "darwin" else
    ""
    )


def handlePremake():
    print(g.parsed_args)
    binary = f"{g.envs['BINARY_DIR']}/premake/{premakeFileName}{osExecExtension}"
    args = g.parsed_args.premake_args  # This is already a list

    cmd = [binary] + args

    subprocess.run(cmd, check=True)






def premakeExists() -> bool:
    if utils.fileExists(f"{g.envs["BINARY_DIR"]}/premake/{premakeFileName}"):
        return True
    return False

def getPremake():
    osName = (
    "windows" if platform.system().lower() == "windows" else
    "linux" if platform.system().lower() == "linux" else
    "macosx" if platform.system().lower() == "darwin" else
    "unknown"
    )
    osExtention = (

    "zip" if platform.system().lower() == "windows" else
    "tar.gz" if platform.system().lower() == "linux" else
    "tar.gz" if platform.system().lower() == "darwin" else
    "unknown"
    )


    utils.downloadFile(f"https://github.com/premake/premake-core/releases/download/v{g.envs["PREMAKE_VERSION"]}/premake-{g.envs["PREMAKE_VERSION"]}-{osName}.{osExtention}",
                       f"{g.envs["TEMP_DIR"]}/premake.{osExtention}")
    utils.extract(f"{g.envs["TEMP_DIR"]}/premake.{osExtention}",f"{g.envs["BINARY_DIR"]}/premake")