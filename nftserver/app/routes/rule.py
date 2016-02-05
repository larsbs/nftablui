from flask import jsonify, request
from wrappers import rule_wrapper
from validators import rule_validator
from utils.nft_errors import abort, NFTError, NFTValidationError


def rules():
    '''
    GET:
      List all rules in the system
    POST:
      Create a new rule in the system
    '''
    if request.method == 'POST':
        try:
            rule_json = rule_validator.validate_new_rule(request.get_json())
            rule = rule_wrapper.create_rule(rule_json)
            response = jsonify(rule=rule)
            response.status_code = 201
            return response
        except NFTValidationError as e:
            return abort(400, e)
        except NFTError as e:
            return abort(500, e)
    else:
        return jsonify(rules=rule_wrapper.list_all_rules())


def rule(rule_id):
    '''
    GET:
      Get a rule by it's id
    DELETE:
      Delete the rule with the specified id
    '''
    if request.method == 'DELETE':
        try:
            rule = rule_validator.validate_rule_delete(rule_id)
            rule = rule_wrapper.delete_rule(rule_id)
            response = jsonify({})
            response.status_code = 204
            return response
        except NFTValidationError as e:
            return abort(400, e)
        except NFTError as e:
            return abort(500, e)
    else:
        return jsonify(rule=rule_wrapper.get_rule(rule_id))
