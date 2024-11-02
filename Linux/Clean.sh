#!/bin/bash

binaryDir="Vendor/Binaries"

echo "Cleaning Project..."
pushd "$(dirname "$0")/../../" > /dev/null

if [ ! -d "$binaryDir/venv" ]; then
    echo "Virtual environment directory not found. Exiting..."
    popd > /dev/null
    exit 1
fi

if [ ! -f "$binaryDir/venv/bin/activate" ]; then
    echo "Virtual environment activation script not found. Exiting..."
    popd > /dev/null
    exit 1
fi

echo "Activating virtual environment..."
source "$binaryDir/venv/bin/activate"

python Scripts/Python/Clean.py "$1"

if [ "$1" == "all" ]; then
    echo "Cleaning $binaryDir"
    rm -rf "$binaryDir"
fi

deactivate

popd > /dev/null
