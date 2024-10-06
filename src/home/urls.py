"""URL configuration for the home application."""

from django.urls import re_path
from django.views.generic.base import RedirectView

from home import views

app_name = "home"

urlpatterns = [
    re_path(
        "^$",
        RedirectView.as_view(url="swimming/"),
        name="home_html",
    ),
    re_path(
        "^favicon.svg$",
        views.favicon,
        name="favicon",
    ),
    re_path(
        "^favicon.ico$",
        views.favicon,
    ),
]
