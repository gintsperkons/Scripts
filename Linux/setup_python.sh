#!bin/bash

source Scripts/Linux/vars.sh

check_python() {  
  output="$(python3 -c "print(1+1)")"
  if [[ $output -ne 2 ]]; then
      echo "Python is not working correctly check your installation."
      exit 1
  fi

  if [ ! -f ""${PWD}/${env_vars[BINARY_DIR]}"/venv/bin/activate" ]; then
      setup_virtual_env
      source ""${PWD}/${env_vars[BINARY_DIR]}"/venv/bin/activate"
      install_python_requirements
      return 0
  fi
  source ""${PWD}/${env_vars[BINARY_DIR]}"/venv/bin/activate"
  

  return 0
}


setup_virtual_env() {
  echo "⚙️ Setting up virtual environment..."
  python -m venv "${PWD}/${env_vars[BINARY_DIR]}/venv"
}

install_python_requirements() {
  echo "⚙️ Installing Python requirements..."
  pip install requests
}