import sys
import re
import os
import importlib

from flask import Flask, request, url_for, abort, jsonify

from router import app_routes


# INITIALIZATION
app = Flask(__name__)
app.config.from_object(__name__)


# CONFIGURATION
# Load default configuration and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'nft.db'),
    DEBUG = True,
    SECRET_KEY = 'development_key'
))
app.config.from_envvar('FLASK_SETTINGS', silent=True)
app.config.from_pyfile('config.cfg', silent=True)


# ROUTES
for route in app_routes:
    options_and_url = re.split(',\s|\s', route[0])
    route[2].methods = options_and_url[0:-1]
    app.add_url_rule(options_and_url[-1], route[1], route[2], methods=options_and_url[0:-1])


# MAIN
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

