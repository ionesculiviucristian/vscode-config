#!/bin/bash

set -eu

continue_dir="${HOME}/.continue"

mkdir -p "${continue_dir}"

cp "./configs/Continue.continue/config.yaml" "${continue_dir}"

exit 0
