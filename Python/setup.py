import globals as g
import premake

def handleSetup():
    if not premake.premakeExists():
        premake.getPremake()
    else:
        print("Premake already exists.")
        