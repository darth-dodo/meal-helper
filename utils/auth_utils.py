from django.core.exceptions import PermissionDenied
from rest_framework_jwt.settings import api_settings
from django.utils.crypto import get_random_string



def jwt_response_payload_handler(token=None, user=None, request=None):
    """
    Custom JWT payload creator

    /auth/login/ will redirects to this endpoint
    User auth using tokens or user object wrapper around vanilla auth/login

    :param token: JWT token
    :param user: User object
    :param request: Request object
    :return: dict
    """

    if token is None:
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)

    return_data = {
        'auth_token': token,
    }

    return return_data
