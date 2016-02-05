from utils import nft_utils
from utils.nft_errors import NFTError, Error
from parsers import set_parser


def list_all_sets():
    return set_parser.parse_sets(nft_utils.nft_list_ruleset(nna=True))


def get_set(set_id):
    sets = list_all_sets()
    return set_parser.parse_set(set_id, sets)


def create_set(set_json):
    set_json['family'], set_json['table'] = set_json['table'].split(':')
    cmd_string = 'add set {family} {table} {name} {{ type {dataType}; }}'.format(**set_json)
    cmd = nft_utils.nft_command(cmd_string)
    cmd_result = cmd.wait()
    if cmd_result == 0:
        nft_utils.close_nft_command(cmd)
        set = set_json
        set['id'] = '{family}:{table}:{name}'.format(**set_json)
        set['items'] = set['items'] if set['items'] else None
        set['table'] = set['family'] + ':' + set['table']
        return set
    else:
        raise NFTError(Error(cmd.stdout.readlines()))


def update_set(set_json):
    set_json['family'], set_json['table'] = set_json['table'].split(':')
    if set_json['items']:
        cmd_string = 'add element {family} {table} {name} {{ {items} }}'.format(**set_json)
        cmd = nft_utils.nft_command(cmd_string)
        cmd_result = cmd.wait()
    else:
        cmd_result = 0
    if cmd_result == 0:
        nft_utils.close_nft_command(cmd)
        set = set_json
        set['table'] = set['family'] + ':' + set['table']
        return set
    else:
        raise NFTError(Error(cmd.stdout.readlines()))
