from utils.nft_errors import NFTValidationError, abort


def validate_new_set(set_json):
    set = set_json['set']
    validation_error = NFTValidationError('set')
    # JSON errors
    if not set:
        raise abort(400, 'No "set" field in set json')
    # Validation errors
    if not set['name']:
        validation_error.add_error('name', 'Este campo es necesario.')
    if validation_error.has_errors():
        raise validation_error
    else:
        return set


def validate_set_update(set_json):
    set = set_json['set']
    # JSON errors
    if not set:
        raise abort(400, 'No "set" field in set json')
    return set
