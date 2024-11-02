#!/bin/bash

binaryDir="Vendor/Binaries"
tempDir="$binaryDir/Temp"
pythonVersion=3.13.0
pythonVersionSmall=313

echo "Setting up Project..."
pushd "$(dirname "$0")/../../"

checkDir() {
    if [ ! -d "$1" ]; then
        mkdir -p "$1"
    fi
}

setupVirtualEnv() {
    echo "Creating virtual environment..."
    python -m venv Vendor/Binaries/venv

    echo "Activating virtual environment..."
    source Vendor/Binaries/venv/bin/activate
    pip install -r Scripts/Python/requirements.txt
}



checkDir "$tempDir"

output="$(python -c "print(1+1)")"
if [[ $output -eq 2 ]]; then
    echo "Python is working correctly."
else
    echo "Python is not working correctly."
    exit 1
fi

if [ ! -f "$binaryDir/venv/bin/activate" ]; then
    setupVirtualEnv
else
    echo "Activating virtual environment..."
    source "$binaryDir/venv/bin/activate"
fi

python Scripts/Python/Setup.py "$1"

if [ -d "$tempDir" ]; then
    rm -rf "$tempDir"
fi

echo "Setup complete."
deactivate
popd
