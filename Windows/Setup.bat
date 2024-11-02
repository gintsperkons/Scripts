@echo off
setlocal enabledelayedexpansion
set binaryDir="Vendor\Binaries"
set tempDir="!binaryDir!\Temp"
set pythonVersion=3.13.0
set pythonVersionSmall=313
set pythonURL="https://www.python.org/ftp/python/3.13.0/python-3.13.0-embed-amd64.zip"
set getpipLink="https://bootstrap.pypa.io/get-pip.py"

echo Setting up Project...
pushd "%~dp0../../"

call :checkDir !tempDir!


if not exist "!binaryDir!\Python\python.exe" (
    call :gettingPython
    echo Lib\site-packages>>"!binaryDir!\Python\python!pythonVersionSmall!._pth"
)

if not exist "!binaryDir!\venv\Scripts\activate.bat" (
    call :setupVirtualEnv
) else (
    echo Activating virtual environment...
    call Vendor\Binaries\venv\Scripts\activate.bat
)


python Scripts/Python/Setup.py %1

if exist !tempDir! (
    rmdir /s /q !tempDir!
)

echo Setup complete.
call Vendor\Binaries\venv\Scripts\deactivate.bat
popd
goto :eof


@REM Functions

:checkDir
if not exist %1 (
    mkdir %1
)
exit /b 0


:setupVirtualEnv
    echo Installing virtualenv
    "!binaryDir!\Python\python.exe" -m pip install virtualenv

    echo Creating virtual environment...
    Vendor\Binaries\Python\python.exe -m virtualenv Vendor/Binaries/venv

    echo Activating virtual environment...
    call Vendor\Binaries\venv\Scripts\activate.bat
    pip install -r Scripts/Python/requirements.txt
    exit /b 0

:gettingPython
echo Downloading Python...
powershell -Command "Invoke-WebRequest -Uri !pythonURL! -OutFile Vendor/Binaries/Temp/python.zip"

echo Extracting Python...
powershell -Command "Expand-Archive -Path Vendor/Binaries/Temp/python.zip -DestinationPath Vendor/Binaries/Python"

echo Downloading get-pip.py 
powershell.exe -Command "Invoke-WebRequest -Uri '!getpipLink!'  -OutFile '!binaryDir!\Temp\get-pip.py'"

echo Installing pip
"!binaryDir!\Python\python.exe" "!binaryDir!\Temp\get-pip.py"

exit /b 0

