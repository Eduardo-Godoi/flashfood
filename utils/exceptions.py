from rest_framework.exceptions import APIException


class UnprocessableEntity(APIException):

    status_code = 422
    default_detail = "You already made this review."
    default_code = "unprocessable_entity"


class BadRequest(APIException):

    status_code = 400
    default_detail = "You need to place an order first."
    default_code = "bad_request"


class Unauthorized(APIException):

    status_code = 401
    default_detail = "This store does not belong to you"
    default_code = " Unauthorized"
