from flask import jsonify, request

from wrappers import dictionary_wrapper
from validators import dictionary_validator
from utils.nft_errors import abort, NFTError, NFTValidationError


def dictionaries():
    '''
    GET:
      List all dictionaries in the system
    POST:
      Create a new dictionary in the system
    '''
    if request.method == 'POST':
        try:
            dictionary_json = dictionary_validator.validate_new_dictionary(request.get_json())
            dictionary = dictionary_wrapper.create_dictionary(dictionary_json)
            return jsonify(dictionary=dictionary)
        except NFTValidationError as e:
            return abort(400, e)
        except NFTError as e:
            return abort(500, e)
    else:
        return jsonify(dictionaries=dictionary_wrapper.list_all_dictionaries())


def dictionary(dictionary_id):
    '''
    GET:
      Get a dictionary by it's id
    PUT:
      Update the dictionary with the specified id
    '''
    if request.method == 'PUT':
        try:
            dictionary_json = dictionary_validator.validate_dictionary_update(request.get_json())
            dictionary = dictionary_wrapper.update_dictionary(dictionary_json)
            return jsonify(dictionary=dictionary)
        except NFTValidationError as e:
            return abort(400, e)
        except NFTError as e:
            return abort(500, e)
    else:
        return jsonify(dictionary=dictionary_wrapper.get_dictionary(dictionary_id))
