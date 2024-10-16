from django.urls import re_path

from illallangi.django.swimming import views

urlpatterns = [
    re_path(
        "^$",
        views.swims_html,
        name="swims_html",
    ),
    re_path(
        r"^(?P<swim_year>[0-9]{4})/$",
        views.swims_html,
        name="swims_year",
    ),
    re_path(
        r"^(?P<swim_year>[0-9]{4})/(?P<swim_month>[0-9]{2})/$",
        views.swims_html,
        name="swims_month",
    ),
    re_path(
        r"^(?P<swim_year>[0-9]{4})/(?P<swim_month>[0-9]{2})/(?P<swim_day>[0-9]{2})/$",
        views.swims_html,
        name="swims_day",
    ),
    re_path(
        r"^(?P<swim_year>[0-9]{4})/(?P<swim_month>[0-9]{2})/(?P<swim_day>[0-9]{2})/(?P<swim_slug>[\w\d-]+)/$",
        views.swim_html,
        name="swim_html",
    ),
]
