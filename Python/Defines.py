import os
binaryDir = "Vendor/Binaries/"
compileDir = "Binaries/"
tempDir = f"{binaryDir}Temp/"
projectPath = os.getcwd()



premakeExtensions = {
    "nt":".exe",
    "posix":""
}
premakePath = f"{binaryDir}Premake/premake5{premakeExtensions[os.name]}"
premakeDir = f"{binaryDir}Premake/"
defaultEnvironment = {
    "nt":"vs2022",
    "posix":"gmake2"
}
premakeURL = {
    "nt":"https://github.com/premake/premake-core/releases/download/v5.0.0-beta4/premake-5.0.0-beta4-windows.zip",
    "posix":"https://github.com/premake/premake-core/releases/download/v5.0.0-beta4/premake-5.0.0-beta4-linux.tar.gz"
}
premakeArchive = {
    "nt":f"{tempDir}premake.zip",
    "posix":f"{tempDir}premake.tar.gz"
}