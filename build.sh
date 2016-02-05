#!/bin/bash


BUILD_DIR='build'
SERVER_DIR='nftserver'
CLIENT_DIR='nftclient'
INSTALL_SCRIPT='install.sh'
RUN_SCRIPT='run.sh'


create_build_dir() {
  echo '## ===================================='
  echo '## Creating build dir...'

  mkdir -p ${BUILD_DIR}

  echo '## Finished'
  echo ''
}


copy_server_code() {
  echo '## ===================================='
  echo '## Copying server code...'

  cp -R ${SERVER_DIR}/app ${BUILD_DIR}/app
  cp -R ${SERVER_DIR}/requirements.txt ${BUILD_DIR}/requirements.txt

  echo '## Finished'
  echo ''
}


build_client_code() {
  echo '## ===================================='
  echo '## Building client code...'

  cd ${CLIENT_DIR}
  ember build --output-path=../${BUILD_DIR}/app/static/
  cd ..

  echo '## Finished'
  echo ''
}


set_server_as_production() {
  echo '## ===================================='
  echo '## Setting server as production...'

  echo 'PRODUCTION=True' > ${BUILD_DIR}/app/config.cfg

  echo '## Finished'
  echo ''
}


copy_server_scripts() {
  echo '## ===================================='
  echo '## Copying server scripts...'

  cp ${INSTALL_SCRIPT} ${BUILD_DIR}/${INSTALL_SCRIPT}
  cp ${RUN_SCRIPT} ${BUILD_DIR}/${RUN_SCRIPT}

  echo '## Finished'
  echo ''
}


clean() {
  rm -rf ${BUILD_DIR}
}


create_build_dir
copy_server_code
build_client_code
set_server_as_production
copy_server_scripts
#clean
