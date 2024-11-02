@echo off
setlocal EnableDelayedExpansion

set binaryDir=Vendor\Binaries

echo Cleaning Project...
pushd "%~dp0../../"


if not exist "!binaryDir!\venv\Scripts\activate.bat" (
    echo Virtual environment not found. Exiting...
    goto :eof
)
echo Activating virtual environment...
call Vendor\Binaries\venv\Scripts\activate.bat

python Scripts/Python/Clean.py %1

if "%1" == "all" (
    if exist !binaryDir! (
    echo Cleaning !binaryDir!
    rmdir /s /q !binaryDir!
    )
)

call deactivate


popd
goto :eof