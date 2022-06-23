from django.http import JsonResponse
from django.conf import settings
import logging
# Get an instance of a logger
logger = logging.getLogger(__name__)

from http import HTTPStatus

def created_response(message="", body={}):
    return success_response(HTTPStatus.CREATED, message=message, body=body)


def paginated_response(http_status_code=HTTPStatus.OK, message="", body={}, pagination={}, **kwargs):
    return success_response(http_status_code, message, body, pagination, **kwargs)


def success_response(http_status_code=HTTPStatus.OK, message="", body={}, pagination=None, **kwargs):
    responseData = {}
    responseData['data'] = body
    responseData['metaData'] = kwargs
    responseData['message'] = message

    if pagination:
        responseData['pagination'] = pagination

    response = JsonResponse(responseData, status=http_status_code, safe=False)

    return response

