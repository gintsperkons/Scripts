#!/bin/bash

binaryDir="Vendor/Binaries"

echo "Cleaning Project..."
pushd "$(dirname "$0")/../../" > /dev/null

if [ ! -f "$binaryDir/venv/bin/activate" ]; then
    echo "Virtual environment not found. Exiting..."
    popd > /dev/null
    exit 1
fi

echo "Activating virtual environment..."
source "$binaryDir/venv/bin/activate"

python Scripts/Python/Clean.py "$1"

if [ "$1" == "all" ]; then
    if [ -d "$binaryDir" ]; then
        echo "Cleaning $binaryDir"
        rm -rf "$binaryDir"
    fi
fi

deactivate

popd > /dev/null
