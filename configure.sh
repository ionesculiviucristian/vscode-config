#!/bin/bash

set -eu

configs_dir="./configs"

find "${configs_dir}" -type d | while read -r dir; do
  if [[ -e "${dir}/setup.sh" ]]; then
    echo "Applying configuration from ${dir}..."
    "./${dir}/setup.sh"
  fi
done

exit 0
