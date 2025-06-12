

# Source the necessary Flux
. .\Flux\Window\utils.ps1
. .\Flux\Window\load_env.ps1
. .\Flux\Window\setup_python.ps1


# Change to the root directory of the project
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Push-Location (Join-Path $scriptDir "..\..")

# Check if the .env file exists and generate it if not
$hasEnv = Check-IfEnvFileExists

if ($hasEnv -ne 0) {
    Gen-Env  # Generate the .env file if it doesn't exist
}
# Load environment variables from the .env file
Load-Env

# Check Python and install requirements
Check-Python

# Run the setup Python script
python3 .\Flux\Python\flux.py @Args

$tempExists = Check-FileExists $env_vars['TEMP_DIR']
if ($tempExists -eq 1) {
    Remove-Item -Path $env_vars['TEMP_DIR'] -Recurse -Force
}
Deactivate-VirtualEnv


if ($args[0] -eq "clean" -and $args[1] -eq "all") {
    Write-Host "⚠️ Cleaning all binaries..."
    
    # Remove the directory recursively and forcefully
    Remove-Item -Path $env_vars.BINARY_DIR -Recurse -Force
}

# Return to the original directory
Pop-Location
