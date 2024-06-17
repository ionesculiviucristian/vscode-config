#!/bin/bash

# set -x

# d9b82aed
# e17cc2af
# 0528f0c8
# e6e9c864
# 61e01458
# 53804979

_R="\033[0m"
_G='\033[0;32m'
_B="\033[0;34m"

BASE_DIR_PATH=~/.config/Code/User
PROFILES_DIR_PATH="${BASE_DIR_PATH}/profiles"
STORAGE_FILE_PATH="${BASE_DIR_PATH}/globalStorage/storage.json"

ENHANCED_NAME="Enhanced"
ENHANCED_LOCATION="-032cba3e"

NAMES=("Python" "php" "Vue")
LOCATIONS=("-4edf6258" "-e01d32a2" "-fa2f2c62")

profile_exists ()
{
  cat $STORAGE_FILE_PATH | jq --arg location $1 'if has("userDataProfiles") then .userDataProfiles | map(select(.location == $location)) | length > 0 else false end'
}

create_profile ()
{
  TEMP_FILE=$(mktemp)
  cp $STORAGE_FILE_PATH $TEMP_FILE
  jq --arg location $1 --arg name $2 'if has("userDataProfiles") then .userDataProfiles += [{"location":$location,"name":$name}] else .userDataProfiles = [{"location":$location,"name":$name}] end' $TEMP_FILE > $STORAGE_FILE_PATH
  rm -f -- $TEMP_FILE
}

install_extensions ()
{
  cat $1 | jq -r --arg profile $2 '.[] | "code --profile \($profile) --install-extension \(.) > /dev/null 2>&1"' | while IFS= read -r line; do
    echo -e "${_B}Installing extension using ${line}${_R}"
    eval "$line"
  done
}

install_profile () 
{
  LOCATION="${PROFILES_DIR_PATH}/${1}"
  LOCAL_PROFILE=./profiles/${2,}
  echo -e "${_G}Installing ${2} profile...${_R}"
  if ! [ -d $LOCATION ]; then
    mkdir -p $LOCATION
  fi
  jq -s ".[0] * .[1]" "./profiles/${ENHANCED_NAME,}/settings.json" "${LOCAL_PROFILE}/settings.json" > "${LOCATION}/settings.json"
  if [ $(profile_exists "${1}") = false ]; then
    create_profile "${1}" "${2}"
  fi
  install_extensions "${LOCAL_PROFILE}/extensions.json" ${2}
}

install_enhanced_profile ()
{
  install_profile ${ENHANCED_LOCATION} ${ENHANCED_NAME}
}

install_profiles ()
{
  install_enhanced_profile
  for ((i = 0; i < ${#LOCATIONS[@]}; i++)); do
    install_profile ${LOCATIONS[i]} ${NAMES[i]}
    install_extensions "./profiles/${ENHANCED_NAME,}/extensions.json" ${NAMES[i]}
  done
}

install_profiles
