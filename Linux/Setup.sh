#!/bin/bash

binaryDir="Vendor/Binaries"
tempDir="$binaryDir/Temp"
pythonVersion=3.13.0
pythonVersionSmall=313
pythonURL="https://www.python.org/ftp/python/3.13.0/python-3.13.0-embed-amd64.zip"
getpipLink="https://bootstrap.pypa.io/get-pip.py"

echo "Setting up Project..."
pushd "$(dirname "$0")/../../"

checkDir() {
    if [ ! -d "$1" ]; then
        mkdir -p "$1"
    fi
}

setupVirtualEnv() {
    echo "Creating virtual environment..."
    python -m virtualenv Vendor/Binaries/venv

    echo "Activating virtual environment..."
    source Vendor/Binaries/venv/bin/activate
    pip install -r Scripts/Python/requirements.txt
}

gettingPython() {
    echo "Downloading Python..."
    curl -o "$tempDir/python.zip" "$pythonURL"

    echo "Extracting Python..."
    unzip "$tempDir/python.zip" -d "$binaryDir/Python"

    echo "Downloading get-pip.py"
    curl -o "$tempDir/get-pip.py" "$getpipLink"

    echo "Installing pip"
    "$binaryDir/Python/python.exe" "$tempDir/get-pip.py"
}

checkDir "$tempDir"

output="$(python -c "print(1+1)")"
if [[ output -eq 2 ]]; then
    gettingPython
    echo "Lib/site-packages" >> "$binaryDir/Python/python$pythonVersionSmall._pth"
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
