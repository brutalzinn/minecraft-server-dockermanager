def error_response(status, message=''):
    return {'status': status, 'data': message}