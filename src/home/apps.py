"""
This module defines the configuration for the 'home' Django application.

Classes:
    HomeConfig(AppConfig): Configuration class for the 'home' app.
"""

from django.apps import AppConfig


class HomeConfig(AppConfig):
    """
    Django application configuration for the Home app.

    Attributes:
        default_auto_field (str): Specifies the type of auto-incrementing primary key to use for models in this app.
        name (str): The full Python path to the application.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "home"
