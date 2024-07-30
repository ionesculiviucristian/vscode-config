#!/bin/bash

# set -eu

RESET="\033[0m"
GREEN="\033[0;32m"
BLUE="\033[0;34m"

BASE_DIR_PATH=~/.config/Code/User
PROFILES_DIR_PATH="${BASE_DIR_PATH}/profiles"
STORAGE_FILE_PATH="${BASE_DIR_PATH}/globalStorage/storage.json"

# Base profile from which all others will be extended
ENHANCED_NAME="Enhanced"
ENHANCED_LOCATION="032cba3e"

# Profile names
NAMES=("Python" "php" "Vue" "Experimental" "React")
# Folders corresponding to each profile defined above
LOCATIONS=("4edf6258" "e01d32a2" "fa2f2c62" "d9b82aed", "e493ba8f")

success ()
{
  echo -e "${GREEN}$1${RESET}"
}

info ()
{
  echo -e "${BLUE}$1${RESET}"
}

strip_comments ()
{
	cat "$1" | sed 's/^ *\/\/.*//'
}

profile_exists ()
{
  cat "${STORAGE_FILE_PATH}" | jq --arg location "$1" 'if has("userDataProfiles") then .userDataProfiles | map(select(.location == $location)) | length > 0 else false end'
}

create_profile ()
{
  TEMP_FILE=$(mktemp)
  cp "${STORAGE_FILE_PATH}" "${TEMP_FILE}"
  # Add or create a new profile entry
  jq --arg location "$1" --arg name "$2" 'if has("userDataProfiles") then .userDataProfiles += [{"location":$location,"name":$name}] else .userDataProfiles = [{"location":$location,"name":$name}] end' "${TEMP_FILE}" > "${STORAGE_FILE_PATH}"
  rm -f "${TEMP_FILE}"
}

install_profile_settings ()
{
  # Merged the enhanced and the specified profile settings
  jq -s ".[0] * .[1]" <(strip_comments "./profiles/${ENHANCED_NAME,}/settings.json") <(strip_comments "$1") > "$2"
}

install_profile_extensions ()
{
  cat "$1" | jq -r --arg profile "$2" '.[] | "info \"Installing extension \(.)...\" && code --profile \($profile) --install-extension \(.) > /dev/null 2>&1"' | while IFS= read -r line; do
    eval "${line}"
  done
}

install_profile () 
{
  LOCATION="${PROFILES_DIR_PATH}/$1"
  LOCAL_PROFILE="./profiles/${2,}"
  success "Installing $2 profile..."
  # Make sure the globalStorage folder is created as it saves the editor's state
  if ! [ -d "${LOCATION}/globalStorage" ]; then
    mkdir -p "${LOCATION}/globalStorage"
  fi
  if [ $(profile_exists "$1") = false ]; then
    create_profile "$1" "$2"
  fi
  install_profile_settings "${LOCAL_PROFILE}/settings.json" "${LOCATION}/settings.json"
  # Speed up extensions installation for profiles extending the Enhanced profile
  if [ -f "${PROFILES_DIR_PATH}/${ENHANCED_LOCATION}/extensions.json" ]; then
    cp "${PROFILES_DIR_PATH}/${ENHANCED_LOCATION}/extensions.json" "${LOCATION}/extensions.json"
  fi
  install_profile_extensions "${LOCAL_PROFILE}/extensions.json" "$2"
}

install_enhanced_profile ()
{
  install_profile "${ENHANCED_LOCATION}" "${ENHANCED_NAME}"
}

install_profiles ()
{
  install_enhanced_profile
  for ((i = 0; i < ${#LOCATIONS[@]}; i++)); do
    install_profile "${LOCATIONS[i]}" "${NAMES[i]}"
    install_profile_extensions "./profiles/${ENHANCED_NAME,}/extensions.json" "${NAMES[i]}"
  done
}

uninstall_profiles ()
{
  success "Uninstalling profiles..."
  rm -rf ${PROFILES_DIR_PATH}
  TEMP_FILE=$(mktemp)
  cp "${STORAGE_FILE_PATH}" "${TEMP_FILE}"
  jq '.userDataProfiles=[]' "${TEMP_FILE}" > "${STORAGE_FILE_PATH}"
  rm -f "${TEMP_FILE}"
}

"$@"
