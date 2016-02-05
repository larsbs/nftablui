#!/bin/bash


USING_VIRTUAL_ENV=false


# Get if using virtual env
if [ -f '.using-venv' ]; then
  USING_VIRTUAL_ENV=true
else
  USING_VIRTUAL_ENV=false
fi


run_using_virtualenv() {
  echo '## ==============================='
  echo '## Running using virtualenv...'
  echo ''
  source '.venv/bin/activate'
  cd app
  sudo python3 app.py
  cd ..
  deactivate
}


run_without_virtualenv() {
  echo '## ==============================='
  echo '## Running without virtualenv...'
  echo ''
  cd app
  sudo python3 app.py
  cd ..
}


if [ "${USING_VIRTUAL_ENV}" = true ]; then
  run_using_virtualenv
else
  run_without_virtualenv
fi
