from flask import jsonify, current_app, send_from_directory


def index(dummy=None):
    if current_app.config['PRODUCTION']:
        return send_from_directory('static/', 'index.html')
    else:
        return send_from_directory('../../nftclient/dist/', 'index.html')


def dist(filename):
    if current_app.config['PRODUCTION']:
        return send_from_directory('static/', filename)
    else:
        return send_from_directory('../../nftclient/dist/', filename)
