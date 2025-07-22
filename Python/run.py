import globals as g


def handleRun():
    import subprocess
    import os
    try:
        if not os.path.exists("Binaries/runtime-debug/MaterialDesignProgram"):
            subprocess.run(["python3","Flux/Python/flux.py", "build"], check=True)
        subprocess.run(["Binaries/runtime-debug/MaterialDesignProgram"], check=True)
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(e) 



