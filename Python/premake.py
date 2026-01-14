import platform
import subprocess

import globals as g
import utils

premakeFileName = "premake5"
osExecExtension = (
    ".exe"
    if platform.system().lower() == "windows"
    else ""
    if platform.system().lower() == "linux"
    else ""
    if platform.system().lower() == "darwin"
    else ""
)


def handlePremake():
    print(g.parsed_args)
    binary = f"{g.envs['BINARY_DIR']}/premake/{premakeFileName}{osExecExtension}"
    args = g.parsed_args.premake_args  # This is already a list

    cmd = [binary] + args
    try:
        import os

        if not os.path.exists("Vendor/Binaries/premake/premake5"):
            subprocess.run(["python3", "Flux/Python/flux.py", "setup"])
        if not (("gmake" in args) or ("vs2022" in args)):
            premake_cmd = cmd + [getDefaultPremakeAction()]
            subprocess.run(premake_cmd, check=True)
            export_cmd = cmd + ["compiledb"]
            subprocess.run(export_cmd, check=True)
    except Exception as e:
        print(e)


def premakeExists() -> bool:
    return False
    if utils.fileExists(f"{g.envs['BINARY_DIR']}/premake/{premakeFileName}"):
        return True
    return False


def getDefaultPremakeAction():
    return (
        "vs2022"
        if platform.system().lower() == "windows"
        else "gmake"
        if platform.system().lower() == "linux"
        else "gmake"
        if platform.system().lower() == "darwin"
        else "gmake"
    )


def getPremake():
    import os
    import shutil

    osName = (
        "windows"
        if platform.system().lower() == "windows"
        else "linux"
        if platform.system().lower() == "linux"
        else "macosx"
        if platform.system().lower() == "darwin"
        else "unknown"
    )
    osExtention = (
        "zip"
        if platform.system().lower() == "windows"
        else "tar.gz"
        if platform.system().lower() == "linux"
        else "tar.gz"
        if platform.system().lower() == "darwin"
        else "unknown"
    )

    utils.downloadFile(
        f"https://github.com/premake/premake-core/releases/download/v{g.envs['PREMAKE_VERSION']}/premake-{g.envs['PREMAKE_VERSION']}-{osName}.{osExtention}",
        f"{g.envs['TEMP_DIR']}/premake.{osExtention}",
    )
    utils.extract(
        f"{g.envs['TEMP_DIR']}/premake.{osExtention}", f"{g.envs['BINARY_DIR']}/premake"
    )

    # --- Download premake-export-compile-commands plugin ---
    plugin_dir = f"{g.envs['BINARY_DIR']}/premake/export-compile-commands"
    if not os.path.exists(plugin_dir):
        utils.downloadFile(
            "https://github.com/akash1474/premake-export-compile-commands/archive/refs/heads/master.zip",
            f"{g.envs['TEMP_DIR']}/premake-export-compile-commands.zip",
        )
        plugin_tmp = f"{g.envs['BINARY_DIR']}/premake/export-compile-commands-tmp"

        utils.extract(
            f"{g.envs['TEMP_DIR']}/premake-export-compile-commands.zip", plugin_tmp
        )

        # The ZIP always contains premake-export-compile-commands-master/
        extracted_folder = os.path.join(
            plugin_tmp, "premake-export-compile-commands-master"
        )
        if os.path.exists(plugin_dir):
            shutil.rmtree(plugin_dir)
        shutil.move(extracted_folder, plugin_dir)
        shutil.rmtree(plugin_tmp, ignore_errors=True)
