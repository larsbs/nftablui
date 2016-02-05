from utils.nft_errors import NFTValidationError, abort
from wrappers import table_wrapper


def validate_new_table(table_json):
    table = table_json.pop('table', None)
    validation_error = NFTValidationError('table')
    # Validation
    if not table:
        validation_error.add_error('table', 'No "table" field in table json')
        raise validation_error
    if not table['name']:
        validation_error.add_error('name', 'Este campo es necesario.')
    if not table['family']:
        validation_error.add_error('family', 'Este campo es necesario.')
    if not table['family'] in ['ip', 'ip6', 'inet', 'bridge', 'arp']:
        validation_error.add_error('family', 'La familia de la tabla no es válida.')
    # Return
    if validation_error.has_errors():
        raise validation_error
    else:
        return table


def validate_table_delete(table_id):
    if not table_id:
        raise abort(400, 'No table id specified.')
    table = table_wrapper.get_table(table_id)
    if not table:
        raise abort(400, 'The table doesn\'t exists')
    return table
