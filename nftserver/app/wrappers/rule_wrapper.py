from utils import nft_utils
from utils.nft_errors import NFTError, Error
from parsers import rule_parser


def list_all_rules():
    return rule_parser.parse_rules(nft_utils.nft_list_ruleset(nna=True))


def get_rule(rule_id):
    rules = list_all_rules()
    return rule_parser.parse_rule(rule_id, rules)


def create_rule(rule_json):
    rule_json['family'], rule_json['tableName'], rule_json['chainName'] = rule_json['chain'].split(':')
    cmd_string = 'add rule {family} {tableName} {chainName} '.format(**rule_json)
    cmd_string += '{expression} {key} '.format(**rule_json)
    cmd_string += nft_utils.statements_to_str(rule_json['statements'])
    cmd = nft_utils.nft_command(cmd_string)
    cmd_result = cmd.wait()
    if cmd_result == 0:
        nft_utils.close_nft_command(cmd)
        from wrappers import chain_wrapper
        rule = rule_json
        # Get handle from last rule added
        rule['handle'] = chain_wrapper.get_chain(rule['chain'])['rules'][-1].split(':')[3]
        rule['id'] = rule['chain'] + ':' + rule['handle']
        return rule
    else:
        raise NFTError(Error(cmd.stdout.readlines()))


def delete_rule(rule_id):
    rule = {}
    rule['family'], rule['tableName'], rule['chainName'], rule['handle'] = rule_id.split(':')
    cmd = nft_utils.nft_command('delete rule {family} {tableName} {chainName} handle {handle}'.format(**rule))
    cmd_result = cmd.wait()
    if cmd_result == 0:
        nft_utils.close_nft_command(cmd)
        return None
    else:
        raise NFTError(Error(cmd.stdout.readlines()))
