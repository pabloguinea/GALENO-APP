

from werkzeug.exceptions import HTTPException

class InvalidRequest(HTTPException):
    code = 400
    description = 'Invalid request.'