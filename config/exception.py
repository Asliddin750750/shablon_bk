from rest_framework.views import exception_handler
from rest_framework.exceptions import ValidationError, PermissionDenied

from config.responses import ResponseFail


def handler(exc, context):
    response = exception_handler(exc, context)

    if isinstance(exc, ValidationError):
        return ResponseFail(exc.detail)

    if isinstance(exc, PermissionDenied):
        return ResponseFail(exc.detail)

    detail = None
    if response is not None:
        if response.data is str:
            detail = response.data
        elif "detail" in response.data:
            detail = response.data["detail"]

    if response is None:
        raise exc

    response.data = {
        "status": "error",
        "data": detail
    }

    return response
