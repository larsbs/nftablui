import os
import time
import tempfile
import subprocess

from flask import make_response, request, jsonify

from utils import nft_utils
from utils.nft_errors import NFTError, abort, Error


def create_backup():
    '''
    GET:
      Generate a backup file and send it to the client
    '''
    file_contents = nft_utils.nft_list_ruleset()
    file_name = 'backup-' + time.strftime('%Y%m%d%H%M%S') + '.nft'
    response = make_response(file_contents)
    response.headers['Content-Disposition'] = 'attachment; filename=' + file_name
    return response


def restore_backup():
    '''
    POST:
      Receive a backup file and load it into the system
    '''
    with tempfile.NamedTemporaryFile(suffix='.nft', delete=False) as tf:
        backup = request.files['file'].read()
        tf.write(backup)
    cmd = nft_utils.nft_command('-f ' + tf.name)
    cmd_result = cmd.wait()
    if cmd_result == 0:
        nft_utils.close_nft_command(cmd)
        os.remove(tf.name)
        return make_response('Backup restored')
    else:
        return abort(500, NFTError(Error(cmd.stdout.read())))
