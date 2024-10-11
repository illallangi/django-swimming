from django.conf import settings
from django.http import HttpRequest


def home_context(
    _: HttpRequest,
) -> dict[str, str]:
    return {
        "HOME_APPS": settings.HOME_APPS,
    }
