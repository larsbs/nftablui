from utils import nft_utils
from utils.nft_errors import NFTError, Error
from parsers import dictionary_parser


def list_all_dictionaries():
    return dictionary_parser.parse_dictionaries(nft_utils.nft_list_ruleset(nna=True))


def get_dictionary(dictionary_id):
    dictionaries = list_all_dictionaries()
    return dictionary_parser.parse_dictionary(dictionary_id, dictionaries)


def create_dictionary(dictionary_json):
    dictionary_json['family'], dictionary_json['table'] = dictionary_json['table'].split(':')
    cmd_string = 'add map {family} {table} {name} {{ type {keyDataType}:{valueDataType}; }}'.format(**dictionary_json)
    cmd = nft_utils.nft_command(cmd_string)
    cmd_result = cmd.wait()
    if cmd_result == 0:
        dictionary = dictionary_json
        dictionary['id'] = '{family}:{table}:{name}'.format(**dictionary_json)
        dictionary['items'] = dictionary['items'] if dictionary['items'] else None
        dictionary['table'] = dictionary['family'] + ':' + dictionary['table']
        return dictionary
    else:
        raise NFTError(Error(cmd.stdout.readlines()))


def update_dictionary(dictionary_json):
    dictionary_json['family'], dictionary_json['table'] = dictionary_json['table'].split(':')
    if dictionary_json['items']:
        cmd_string = 'add element {family} {table} {name} {{ {items} }}'.format(**dictionary_json)
        cmd = nft_utils.nft_command(cmd_string)
        cmd_result = cmd.wait()
    else:
        cmd_result = 0
    if cmd_result == 0:
        dictionary = dictionary_json
        dictionary['table'] = dictionary['family'] + ':' + dictionary['table']
        return dictionary
    else:
        raise NFTError(Error(cmd.stdout.readlines()))
