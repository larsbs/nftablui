from utils.nft_errors import NFTValidationError, abort
from wrappers import rule_wrapper


def validate_new_rule(rule_json):
    rule = rule_json.pop('rule', None)
    validation_error = NFTValidationError('rule')
    # JSON errors
    if not rule:
        validation_error.add_error('rule', 'No "rule" field in rule json')
        raise validation_error
    # Return
    if validation_error.has_errors():
        raise validation_error
    else:
        return rule


def validate_rule_delete(rule_id):
    if not rule_id:
        pass
    rule = rule_wrapper.get_rule(rule_id)
    if not rule:
        pass
    return rule
