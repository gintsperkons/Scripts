@echo off
setlocal EnableDelayedExpansion

set binaryDir=Vendor\Binaries

echo Cleaning Project...
pushd "%~dp0../../"


if not exist "!binaryDir!\venv\Flux\activate.bat" (
    echo Virtual environment not found. Exiting...
    goto :eof
)
echo Activating virtual environment...
call Vendor\Binaries\venv\Flux\activate.bat

python Flux/Python/Clean.py %1

if "%1" == "all" (
    if exist !binaryDir! (
    echo Cleaning !binaryDir!
    rmdir /s /q !binaryDir!
    )
)

call Vendor\Binaries\venv\Flux\deactivate.bat


popd
goto :eof