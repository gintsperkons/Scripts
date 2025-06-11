import globals as g
import premake

def handleSetup():
    if not premake.premakeExists():
        print("init premake code")