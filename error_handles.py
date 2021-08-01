from app import app
from flask import jsonify, request


# 404 handler
@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'There is no record: ' + request.url,
    }
    res = jsonify(message)
    res.status_code = 404
    return res
# end 404 handler


# 403 handler
@app.errorhandler(403)
def forbidden(error=None):
    message = {
        'status': 403,
        'message': 'Forbidden',
    }
    res = jsonify(message)
    res.status_code = 403
    return res
# end 403 handler

# 500 handler


@app.errorhandler(500)
def internal_server_error(error=None):
    message = {
        'status': 500,
        'message': 'Failed to process request',
    }
    res = jsonify(message)
    res.status_code = 500
    traceback.print_exc()
    return res
# end 500 handler
