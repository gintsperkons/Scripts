import os
import globals

def load_env_file(path):
    env = {}
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8-sig") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, value = line.split("=", 1)
                    env[key.strip()] = value.strip()
    return env

def load_env():
    default_env_path = os.path.join("Flux", "defaults/.env_default")
    default_env = load_env_file(default_env_path)

    if os.path.exists(".env"):
        override_env = load_env_file(".env")
        default_env.update(override_env)

    return default_env