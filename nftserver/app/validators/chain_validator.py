from utils.nft_errors import NFTValidationError, abort
from wrappers import table_wrapper, chain_wrapper


def validate_new_chain(chain_json):
    chain = chain_json['chain']
    validation_error = NFTValidationError('chain')
    # JSON errors
    if not chain:
        raise abort(400, 'No "chain" field in chain json')
    if not chain['table']:
        raise abort(400, 'Chain has no table associated')
    if not chain['table'] in [t['id'] for t in table_wrapper.list_all_tables()]:
        raise abort(400, 'The table {table_id} doesn\'t exist'.format(chain['table']))
    # Validate hook and type?
    # Validation errors
    if not chain['name']:
        validation_error.add_error('name', 'Este campo es necesario.')
    # If no hook or type is specified, no priority is needed
    # if chain['priority'] == None:  # Use this instead of "not" because 0 is true
        # validation_error.errors.append({'priority': 'Este campo es necesario.'})
    # Return
    if validation_error.has_errors():
        raise validation_error
    else:
        return chain


def validate_chain_delete(chain_id):
    if not chain_id:
        raise abort(400, 'No chain id specified.')
    chain = chain_wrapper.get_chain(chain_id)
    if not chain:
        raise abort(400, 'The chain doesn\'t exists')
    return chain
