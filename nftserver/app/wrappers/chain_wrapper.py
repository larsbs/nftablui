from utils import nft_utils
from utils.nft_errors import NFTError, Error
from parsers import chain_parser
from wrappers import rule_wrapper


def list_all_chains():
    chains = chain_parser.parse_chains(nft_utils.nft_get_json_command())
    rules = rule_wrapper.list_all_rules()
    chains = nft_utils.join_chains_with_rules(chains, rules)
    return chains


def get_chain(chain_id):
    chains = list_all_chains()
    return chain_parser.parse_chain(chain_id, chains)


def create_chain(chain_json):
    chain_json['family'], chain_json['tableName'] = chain_json['table'].split(':')
    cmd_string = 'add chain {family} {tableName} {name}'.format(**chain_json)
    if chain_json['hook'] and chain_json['type'] and not chain_json['priority'] == None:
        cmd_string += ' {{ type {type} hook {hook} priority {priority} ; }}'.format(**chain_json)
    cmd = nft_utils.nft_command(cmd_string)
    cmd_result = cmd.wait()
    if cmd_result == 0:
        nft_utils.close_nft_command(cmd)
        chain = chain_json
        chain['id'] = '{family}:{tableName}:{name}'.format(**chain_json)
        return chain
    else:
        raise NFTError(Error(cmd.stdout.readlines()))


def flush_chain(chain_id):
    chain = get_chain(chain_id)
    chain['family'], chain['tableName'] = chain['table'].split(':')
    cmd = nft_utils.nft_command('flush chain {family} {tableName} {name}'.format(**chain))
    cmd_result = cmd.wait()
    if cmd_result == 0:
        nft_utils.close_nft_command(cmd)
        chain['id'] = '{family}:{tableName}:{name}'.format(**chain)
        return chain
    else:
        raise NFTError(Error(cmd.stdout.readlines()))


def delete_chain(chain_id):
    chain = flush_chain(chain_id)
    cmd = nft_utils.nft_command('delete chain {family} {tableName} {name}'.format(**chain))
    cmd_result = cmd.wait()
    if cmd_result == 0:
        nft_utils.close_nft_command(cmd)
        chain['id'] = '{family}:{tableName}:{name}'.format(**chain)
        return chain
    else:
        raise NFTError(Error(cmd.stdout.readlines()))
