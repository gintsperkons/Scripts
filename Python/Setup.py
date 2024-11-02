import json
import os
import sys
import shutil
import stat
import Utils
import Defines




def SetupCallerFiles(templates):
    for key, value in templates.items():
        extension = ".bat" if os.name == "nt" else ".sh" 
        fileName = key+extension
        fileData = value[os.name]
        with open(fileName,"w+",encoding="utf-8") as f:
            f.writelines(fileData)
        os.chmod(fileName, stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR | stat.S_IRGRP | stat.S_IROTH)



def SetupPremake():
    print("Setting up premake")
    if not os.path.exists(Defines.premakeDir):
        Utils.downloadFile(Defines.premakeURL[os.name],Defines.premakeArchive[os.name])
        Utils.extract(Defines.premakeArchive[os.name],Defines.premakeDir)
        
    
def ConfiguringPremake(env = Defines.defaultEnvironment[os.name]):
    print("Configuring premake")
    print(f"call \"{os.getcwd()}/{Defines.premakePath}\" {env}")
    os.system(f"call \"{os.getcwd()}/{Defines.premakePath}\" {env}")



if __name__=="__main__":
    templates = {}
    with open("Scripts/Python/templates.json","r+",encoding="utf-8") as f:
        templates = json.load(f)

    env = sys.argv[1] if len(sys.argv) > 1 else None

    SetupCallerFiles(templates)
    SetupPremake()
    if env:
        ConfiguringPremake(env)
    else:
        ConfiguringPremake()
    