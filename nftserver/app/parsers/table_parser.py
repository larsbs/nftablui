from utils import nft_utils
from parsers import chain_parser


def parse_tables(nft_json):
    tables = []
    for element in nft_json:
        if nft_utils.json_is_a_table(element):
            table = element['table']
            table['id'] = table['family'] + ':' + table['name']
            table.pop('use', None)  # Remove use key
            table.pop('flags', None)  # Remove flags key
            tables.append(table)
    return tables


def parse_table(table_id, tables):
    for table in tables:
        if table['id'] == table_id:
            return table
