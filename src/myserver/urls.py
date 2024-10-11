from django.contrib import admin
from django.urls import include, re_path

urlpatterns = [
    re_path(
        "^admin/",
        admin.site.urls,
    ),
    re_path(
        "^swimming/",
        include("illallangi.django.swimming.urls"),
    ),
    re_path(
        "^",
        include("home.urls"),
    ),
]
