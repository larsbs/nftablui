from flask import jsonify, request

from wrappers import set_wrapper
from validators import set_validator
from utils.nft_errors import abort, NFTError, NFTValidationError


def sets():
    '''
    GET:
      List all sets in the system
    POST:
      Create a new set in the system
    '''
    if request.method == 'POST':
        try:
            set_json = set_validator.validate_new_set(request.get_json())
            set = set_wrapper.create_set(set_json)
            return jsonify(set=set)
        except NFTValidationError as e:
            return abort(400, e)
        except NFTError as e:
            return abort(500, e)
    else:
        return jsonify(sets=set_wrapper.list_all_sets())


def set(set_id):
    '''
    GET:
      Get a set by it's id
    PUT:
      Update a set in the system with the specified id
    '''
    if request.method == 'PUT':
        try:
            set_json = set_validator.validate_set_update(request.get_json())
            set = set_wrapper.update_set(set_json)
            return jsonify(set=set)
        except NFTValidationError as e:
            return abort(400, e)
        except NFTError as e:
            return abort(500, e)
    else:
        return jsonify(set=set_wrapper.get_set(set_id))
