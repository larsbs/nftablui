from utils.nft_errors import NFTValidationError, abort


def validate_new_dictionary(dictionary_json):
    dictionary = dictionary_json['dictionary']
    validation_error = NFTValidationError('dictionary')
    # JSON errors
    if not dictionary:
        raise abort(400, 'No "dictionary" field in dictionary json')
    # Validation errors
    if not dictionary['name']:
        validation_error.add_error('name', 'Este campo es necesario.')
    if validation_error.has_errors():
        raise validation_error
    else:
        return dictionary


def validate_dictionary_update(dictionary_json):
    dictionary = dictionary_json['dictionary']
    # JSON errors
    if not dictionary:
        raise abort(400, 'No "dictionary" field in dictionary json')
    return dictionary
