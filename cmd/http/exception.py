import json
from http import HTTPStatus


class ApiError(Exception):
    def __init__(self, message: str, status: int, error_code: str | None = None):
        super().__init__(message)
        self.message = message
        self.status = status
        self.error_code = error_code
        print("ApiError, msg:", message)

    def dump(self):
        return json.dumps({"message": self.message, "code": self.error_code})


class BadRequestError(ApiError):
    def __init__(self, message: str,  error_code: str | None = None):
        super().__init__(message=message, error_code=error_code, status=HTTPStatus.BAD_REQUEST)


class NotFoundError(ApiError):
    def __init__(self, message: str,  error_code: str | None = None):
        super().__init__(message=message, error_code=error_code, status=HTTPStatus.NOT_FOUND)


class ForbiddenError(ApiError):
    def __init__(self, message: str,  error_code: str | None = None):
        super().__init__(message=message, error_code=error_code, status=HTTPStatus.FORBIDDEN)


class InternalError(ApiError):
    def __init__(self, message: str,  error_code: str | None = None):
        super().__init__(message=message, error_code=error_code, status=HTTPStatus.INTERNAL_SERVER_ERROR)


class UnAuthorizedError(ApiError):
    def __init__(self, message: str,  error_code: str | None = None):
        super().__init__(message=message, error_code=error_code, status=HTTPStatus.UNAUTHORIZED)
