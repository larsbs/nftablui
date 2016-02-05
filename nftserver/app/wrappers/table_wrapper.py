from utils import nft_utils
from utils.nft_errors import NFTError, Error
from parsers import table_parser
from wrappers import chain_wrapper, set_wrapper, dictionary_wrapper


def list_all_tables():
    tables = table_parser.parse_tables(nft_utils.nft_get_json_command())
    chains = chain_wrapper.list_all_chains()
    sets = set_wrapper.list_all_sets()
    dictionaries = dictionary_wrapper.list_all_dictionaries()
    tables = nft_utils.join_tables_with_chains(tables, chains)
    tables = nft_utils.join_tables_with_sets(tables, sets)
    tables = nft_utils.join_tables_with_dictionaries(tables, dictionaries)
    return tables


def get_table(table_id):
    tables = list_all_tables()
    return table_parser.parse_table(table_id, tables)


def create_table(table_json):
    cmd = nft_utils.nft_command('add table {family} {name}'.format(**table_json))
    cmd_result = cmd.wait()
    if cmd_result == 0:
        nft_utils.close_nft_command(cmd)
        table = table_json
        table['id'] = '{family}:{name}'.format(**table)
        table['chains'], table['sets'], table['dictionaries'] = ([],[],[])
        return table
    else:
        raise NFTError(Error(cmd.stdout.readlines()))


def flush_table(table_id):
    table = get_table(table_id)
    cmd = nft_utils.nft_command('flush table {family} {name}'.format(**table))
    cmd_result = cmd.wait()
    if cmd_result == 0:
        nft_utils.close_nft_command(cmd)
        table['id'] = '{family}:{name}'.format(**table)
        return table
    else:
        raise NFTError(Error(cmd.stdout.readlines()))


def delete_table(table_id):
    table = flush_table(table_id)
    for chain_id in table['chains']:
        chain_wrapper.delete_chain(chain_id)
    cmd = nft_utils.nft_command('delete table {family} {name}'.format(**table))
    cmd_result = cmd.wait()
    if cmd_result == 0:
        nft_utils.close_nft_command(cmd)
        table['id'] = '{family}:{name}'.format(**table)
        return table
    else:
        raise NFTError(Error(cmd.stdout.readlines()))
