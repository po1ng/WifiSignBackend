from app.constants import constants

def response_dict(status, message='', data=None):
    if not message:
        message = constants[status]
    if data is None:
        data = {}
    return {'status': status, 'message': message, 'data': data}