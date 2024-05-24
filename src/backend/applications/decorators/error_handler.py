from rest_framework.exceptions import ValidationError, NotFound
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from applications.model.errors import *
from applications.serializers.errors import UnprocessableEntityErrorSerializer
from rest_framework import status

def handle_error(func):
    def wrapper(*args, **kwargs) -> Response:
        try:
            return func(*args, **kwargs)
        except (KeyError, ObjectDoesNotExist) as e:
            raise NotFound(e)
        except ValueError as e:
            raise ValidationError(e)
        except UnprocessableEntityError as e:
            return Response(data=UnprocessableEntityErrorSerializer({'error':e}).data, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    return wrapper