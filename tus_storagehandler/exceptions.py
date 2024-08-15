"""Tus Storage Handler exceptions."""

from werkzeug.exceptions import BadRequest, InternalServerError, NotFound
from http import HTTPStatus

exceptions = {
    Exception: {
        "message": "An unexpected error occurred. Please try again.",
        "code": HTTPStatus.INTERNAL_SERVER_ERROR,  # 500
    },
    BadRequest: {
        "message": "Invalid request. Please check your input and try again.",
        "code": HTTPStatus.BAD_REQUEST,  # 400
    },
    NotFound: {
        "message": "The requested resource could not be found.",
        "code": HTTPStatus.NOT_FOUND,  # 404
    },
    InternalServerError: {
        "message": "An internal server error occurred in the tus storage handler",
        "code": HTTPStatus.INTERNAL_SERVER_ERROR,  # 500
    },
}
