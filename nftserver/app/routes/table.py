from flask import jsonify, request, make_response
from wrappers import table_wrapper
from validators import table_validator
from utils.nft_errors import abort, NFTError, NFTValidationError


def tables():
    '''
    GET:
      List all tables in the system
    POST:
      Create a new table in the system
    '''
    if request.method == 'POST':
        try:
            table_json = table_validator.validate_new_table(request.get_json())
            table = table_wrapper.create_table(table_json)
            response = jsonify(table=table)
            response.status_code = 201
            return response
        except NFTValidationError as e:
            return abort(400, e)
        except NFTError as e:
            return abort(500, e)
    else:
        return jsonify(tables=table_wrapper.list_all_tables())


def table(table_id):
    '''
    GET:
      Get a table by it's id
    DELETE:
      Delete the table with the specified id
    '''
    if request.method == 'DELETE':
        try:
            table = table_validator.validate_table_delete(table_id)
            table = table_wrapper.delete_table(table_id)
            response = make_response()
            response.status_code = 204
            return response
        except NFTValidationError as e:
            return abort(400, e)
        except NFTError as e:
            return abort(500, e)
    else:
        return jsonify(table=table_wrapper.get_table(table_id))
