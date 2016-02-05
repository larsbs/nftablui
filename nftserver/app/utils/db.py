import flask
import sqlite3


# DATABASE SCHEMA
DATABASE_SCHEMA = '''
DROP TABLE IF EXISTS tables;
DROP TABLE IF EXISTS chains;
DROP TABLE IF EXISTS rules;

CREATE TABLE tables(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    family TEXT NOT NULL DEFAULT ip
);

CREATE TABLE chains(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    table_id INTEGER REFERENCES tables(id),
    name TEXT NOT NULL,
    type TEXT,
    hook TEXT
);

CREATE TABLE rules(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    chain_id INTEGER REFERENCES chains(id),
    handle INTEGER NOT NULL,
    position INTEGER NOT NULL
);
'''


def get_db():
    '''
    Opens a new database connection if there is none yet
    for the current application context.
    '''
    if not hasattr(flask.g, 'sqlite_db'):
        rv = sqlite3.connect(flask.current_app.config['DATABASE'])
        rv.row_factory = sqlite3.Row
        flask.g.sqlite_db = rv
    return flask.g.sqlite_db


def create_db():
    '''
    Creates the db from the schema.
    '''
    db = get_db()
    db.cursor().executescript(DATABASE_SCHEMA)
    db.commit()


@flask.current_app.teardown_appcontext
def close_db(error):
    '''
    Closes the database again at the end of the request.
    '''
    if hasattr(flask.g, 'sqlite_db'):
        flask.g.sqlite_db.close()
