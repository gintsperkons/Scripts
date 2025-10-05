import globals as g


binPath = "Binaries/runtime-debug/" + g.envs["PROJECT_NAME"]

def run():
    import subprocess
    import os

    try:
        if not os.path.exists(binPath):
            subprocess.run(["python3", "Flux/Python/flux.py", "build"], check=True)
        subprocess.run([binPath], check=True)
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(e)


def runRebuild():
    import subprocess
   
    try:
        subprocess.run(["python3", "Flux/Python/flux.py", "build"], check=True)
        subprocess.run([binPath], check=True)
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(e)


def handleRun():
    if g.parsed_args.command == "run:build":
        runRebuild()
    if g.parsed_args.command == "run":
        run()
