#!/bin/bash


USE_VIRTUAL_ENV=false
REQUIREMENTS_FILE='requirements.txt'


# Get selected task
if [ "$#" -gt 0 ]; then
  if [ "$1" == "-v" ]; then
    USE_VIRTUAL_ENV=true
  fi
fi


install_using_virtualenv() {
  echo '## ===================================='
  echo '## Installing using virtual env...'

  sudo pip install virtualenv
  mkdir -p '.venv'
  virtualenv '.venv'
  source '.venv/bin/activate'
  pip install -r ${REQUIREMENTS_FILE}
  touch '.using-venv'
  deactivate

  echo '## Finished'
  echo ''
}


install_without_virtualenv() {
  echo '## ===================================='
  echo '## Installing without virtual env...'

  sudo pip install -r ${REQUIREMENTS_FILE}
  rm -rf '.using-venv'

  echo '## Finished'
  echo ''
}


if [ "${USE_VIRTUAL_ENV}" = true ]; then
  install_using_virtualenv
else
  install_without_virtualenv
fi
