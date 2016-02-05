from flask import jsonify, request

from wrappers import chain_wrapper
from validators import chain_validator
from utils.nft_errors import abort, NFTError, NFTValidationError


def chains():
    '''
    GET:
      List all chains in the system
    POST:
      Create a new chain in the system
    '''
    if request.method == 'POST':
        try:
            chain_json = chain_validator.validate_new_chain(request.get_json())
            chain = chain_wrapper.create_chain(chain_json)
            r = jsonify(chain=chain)
            r.status_code = 201
            return r
        except NFTValidationError as e:
            return abort(400, e)
        except NFTError as e:
            return abort(500, e)
    else:
        return jsonify(chains=chain_wrapper.list_all_chains())


def chain(chain_id):
    '''
    GET:
      Get a chain by it's id
    DELETE:
      Delete the chain with the specified id
    '''
    if request.method == 'DELETE':
        try:
            chain = chain_validator.validate_chain_delete(chain_id)
            chain = chain_wrapper.delete_chain(chain_id)
            return jsonify(chain=chain)
        except NFTValidationError as e:
            return abort(400, e)
        except NFTError as e:
            return abort(500, e)
    else:
        return jsonify(chain=chain_wrapper.get_chain(chain_id))
