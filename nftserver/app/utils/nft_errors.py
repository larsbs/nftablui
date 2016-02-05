from flask import jsonify


class Error(object):
    '''
    Parse an error response from nftables
    '''
    def __init__(self, message):
        super(Error, self).__init__()
        message = message[0]  # Normally we only want the first line of the error message
        if '<cmdline>' in message:
            message = message[message.find('Error: ') + len('Error: '):].capitalize()
        self.message = message.rstrip('\r\n')

    def as_json(self):
        return {'message': self.message}


class NFTError(Exception):
    def __init__(self, error):
        super(NFTError, self).__init__(error.message)
        self.error = error

    def as_json(self):
        return {'message': self.error.message}


class NFTValidationError(Exception):
    def __init__(self, entity, errors={}):
        super(NFTValidationError, self).__init__('Algunos de los datos introducidos no son correctos. Para más detalles mirar la consola.')
        self.entity = entity
        self.errors = {}

    def add_error(self, field, message):
        self.errors[field] = self.errors[field] if field in self.errors.keys() else []
        self.errors[field].append(message)

    def has_errors(self):
        return len(self.errors.keys()) > 0

    def as_json(self):
        self.errors.update({'message': str(self), 'entity': self.entity})
        return self.errors


def abort(status_code, error=None):
    response = jsonify({})
    if error:
        response = jsonify(errors=error.as_json())
    response.status_code = status_code
    return response
