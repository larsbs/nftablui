import re
import json
import subprocess

from utils.nft_errors import NFTError, Error


def nft_command(command):
    cmd = subprocess.Popen(
        # Find anything between {} or something that isn't a space.
        ['nft'] + re.findall(r'\{[^\}]*\}|\S+', command),
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        universal_newlines=True
    )
    return cmd


def close_nft_command(cmd):
    if cmd.stdin:
        cmd.stdin.close()
    if cmd.stdout:
        cmd.stdout.close()
    if cmd.stderr:
        cmd.stderr.close()


def nft_get_json_command(as_str=False):
    cmd = nft_command('export json')
    cmd_result = cmd.wait()
    if cmd_result == 0:
        if as_str:
            nft_json = cmd.stdout.read()
        else:
            nft_json = json.loads(cmd.stdout.read())['nftables']
        close_nft_command(cmd)
        return nft_json
    else:
        raise NFTError(Error(cmd.stdout.readlines()))


def nft_list_ruleset(nna=False):
    if nna:
        cmd = nft_command('list ruleset -nna')
    else:
        cmd = nft_command('list ruleset')
    cmd_result = cmd.wait()
    if cmd_result == 0:
        if nna:
            ruleset = cmd.stdout.readlines()
        else:
            ruleset = cmd.stdout.read()
        close_nft_command(cmd)
        return ruleset
    else:
        raise NFTError(Error(cmd.stdout.readlines()))


def json_is_a_table(json):
    if len(json.keys()) == 1 and list(json.keys())[0] == 'table':
        return True
    return False


def json_is_a_chain(json):
    if len(json.keys()) == 1 and list(json.keys())[0] == 'chain':
        return True
    return False


def json_is_a_rule(json):
    if len(json.keys()) == 1 and list(json.keys())[0] == 'rule':
        return True
    return False


def find_all_table_chains_ids(table, all_chains):
    table_chains_ids = []
    for chain in all_chains:
        if chain['table'] == table['id']:
            table_chains_ids.append(chain['id'])
    return table_chains_ids


def join_tables_with_chains(tables, chains):
    for table in tables:
        table['chains'] = find_all_table_chains_ids(table, chains)
    return tables


def find_all_chain_rules_ids(chain, all_rules):
    chain_rules_ids = []
    for rule in all_rules:
        if rule['chain'] == chain['id']:
            chain_rules_ids.append(rule['id'])
    return chain_rules_ids


def join_chains_with_rules(chains, rules):
    for chain in chains:
        chain['rules'] = find_all_chain_rules_ids(chain, rules)
    return chains


def find_all_table_sets_ids(table, all_sets):
    table_sets_ids = []
    for set in all_sets:
        if set['table'] == table['id']:
            table_sets_ids.append(set['id'])
    return table_sets_ids


def join_tables_with_sets(tables, sets):
    for table in tables:
        table['sets'] = find_all_table_sets_ids(table, sets)
    return tables


def find_all_table_dictionaries_ids(table, all_dictionaries):
    table_dictionaries_ids = []
    for dictionary in all_dictionaries:
        if dictionary['table'] == table['id']:
            table_dictionaries_ids.append(dictionary['id'])
    return table_dictionaries_ids


def join_tables_with_dictionaries(tables, dictionaries):
    for table in tables:
        table['dictionaries'] = find_all_table_dictionaries_ids(table, dictionaries)
    return tables


def statements_to_str(statements):
    if len(statements) == 1:
        return single_statement_to_str(statements[0])
    elif len(statements) > 1:
        result = 'vmap {'
        for statement in statements:
            result += statement['match'] + ':' + statement['action'] + ', '
        result = result.strip(', ')
        result += '}'
        return result
    return ''


def single_statement_to_str(statement):
    if 'match' in statement.keys():
        return statement['match'] + ' ' + statement['action']
    elif 'set' in statement.keys():
        return statement['set'] + ' ' + statement['action']
    elif 'dictionary' in statement.keys():
        return statement['dictionary']
    return ''
