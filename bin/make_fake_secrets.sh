#!/usr/bin/env sh
#
# This script parse real secrets.yaml-file and based on it
# generate fake one for testing reasons.
#
# Copyright (c) 2019, Andrey "Limych" Khrolenok <andrey@khrolenok.ru>
# Creative Commons BY-NC-SA 4.0 International Public License
# (see LICENSE.md or https://creativecommons.org/licenses/by-nc-sa/4.0/)
#

WDIR=$(cd `dirname $0` && pwd)
ROOT=$(dirname ${WDIR})
SEED=$$

# Define faker callback
faker() {
  local key=$3 value=$4

  if [ "$key" == "ssl_certificate" ]; then
    value='tests/example.com.fake_crt'
  elif [ "$key" == "ssl_key" ]; then
    value='tests/example.com.fake_key'
  elif [ "$key" == "ha_timezone" ]; then
    value='Australia/Sydney'
  elif [ "$key" == "plex_port" ]; then
    value='32400'
  elif echo ${key} | grep -q '_\(date\)$'; then
    value='2019-01-01'
  elif echo ${key} | grep -q '_\(host\|ipaddress\|server\)$'; then
    value='127.0.0.1'
  elif echo ${key} | grep -q '_\(url\)$'; then
    value='http://localhost/somethingsecret'
  elif echo ${key} | grep -q '_\(login\|username\|password\)$'; then
    value='super_5EcREt'
  elif echo ${key} | grep -q '_\(lat\|lon\|latitude\|longitude\)$'; then
    value='00.000000'
  else
    value='SoMeTh1nGsEcrEt'
  fi

  echo "$key: \"$value\""
}



# Include parse_yaml function
. ${WDIR}/_parse_yaml.sh

# Read real yaml file and make fake one
FPATH=${ROOT}/fake_secrets.yaml
>${FPATH}
echo "---"
echo "#" >>${FPATH}
echo "# ATTENTION! This is autogenerated fake file. All values filled random characters." >>${FPATH}
echo "# Don't edit this file -- all changes will be lost on next file auto generation." >>${FPATH}
echo "#" >>${FPATH}
eval $(parse_yaml ${ROOT}/secrets.yaml '' 'faker \"%s\" \"%s\" \"%s\" \"%s\";') >>${FPATH}
echo ""

git commit -m "Automated: Update Fake Secrets" ${ROOT}/fake_secrets.yaml
exit