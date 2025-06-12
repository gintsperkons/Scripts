#!/bin/bash

# Change to the root directory of the project
pushd "$(dirname "$0")/../../"  > /dev/null

# Source the necessary Flux
source Flux/Linux/load_env.sh
source Flux/Linux/setup_python.sh
source Flux/Linux/vars.sh



# Load environment variables from the .env file
load_env

check_python

python3 Flux/Python/flux.py "$@"
deactivate


if [[ "$1" == "clean:all" ]]; then
  echo "⚠️ Cleaning all binaries..."
  rm -rf "${BASE_DIR}/${env_vars[BINARY_DIR]}"
fi

popd  > /dev/null
