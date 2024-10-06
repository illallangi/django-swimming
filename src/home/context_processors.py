"""Context processor for the home app."""

from django.conf import settings
from django.http import HttpRequest


def home_context(
    _: HttpRequest,
) -> dict[str, str]:
    """Return the context for the home app."""
    return {
        "HOME_APPS": settings.HOME_APPS,
    }
