from routes.table import tables, table
from routes.chain import chains, chain
from routes.rule import rules, rule
from routes.set import sets, set
from routes.dictionary import dictionaries, dictionary
from routes.app import index, dist
from routes.files import create_backup, restore_backup


# APP URLS
app_routes = [
    # APP
    ['GET /', 'index', index],
    ['GET /<path:filename>', 'dist', dist],
    ['GET /tables/<dummy>', 'index', index],
    ['GET /table/<dummy>', 'index', index],
    ['GET /chain/<dummy>', 'index', index],
    ['GET /sets', 'index', index],
    ['GET /dictionaries', 'index', index],
    ['GET /files', 'index', index],

    # Tables
    ['GET, POST /api/tables', 'tables', tables],
    ['GET, DELETE /api/tables/<table_id>', 'table', table],

    # Chains
    ['GET, POST /api/chains', 'chains', chains],
    ['GET, DELETE /api/chains/<chain_id>', 'chain', chain],

    # Rules
    ['GET, POST /api/rules', 'rules', rules],
    ['GET, DELETE /api/rules/<rule_id>', 'rule', rule],

    # Sets
    ['GET, POST /api/sets', 'sets', sets],
    ['GET, PUT, DELETE /api/sets/<set_id>', 'set', set],

    # Dictionaries
    ['GET, POST /api/dictionaries', 'dictionaries', dictionaries],
    ['GET, PUT, DELETE /api/dictionaries/<dictionary_id>', 'dictionary', dictionary],

    # Files
    ['GET /create-backup', 'create_backup', create_backup],
    ['GET, POST /restore-backup', 'restore_backup', restore_backup]
]
