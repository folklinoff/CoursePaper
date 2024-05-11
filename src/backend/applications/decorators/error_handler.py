from rest_framework.exceptions import ValidationError, NotFound
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response


def handle_error(func):
    def wrapper(*args, **kwargs) -> Response:
        try:
            return func(*args, **kwargs)
        except (KeyError, ObjectDoesNotExist) as e:
            raise NotFound(e)
        except ValueError as e:
            raise ValidationError(e)
    return wrapper