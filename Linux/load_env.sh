#!/bin/bash

declare -A env_vars

# Load key-value pairs from a file into env_vars (override existing keys)
load_env_file() {
  local file="$1"
  if [ -f "$file" ]; then
    while IFS='=' read -r key value; do
      # Skip comments and empty lines
      if [[ "$key" != \#* && -n "$key" ]]; then
        env_vars["$key"]="$value"
      fi
    done < "$file"
  else
    echo "⚠️ Env file '$file' not found!"
  fi
}

# Load defaults and overrides
load_env() {
  load_env_file "Flux/defaults/.env_default"

  if [ -f ".env" ]; then
    load_env_file ".env"
  fi
}