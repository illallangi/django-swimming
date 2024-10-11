from django.urls import include, re_path

from illallangi.django.swimming import views

app_name = "swimming"

urlpatterns = [
    re_path(
        "^$",
        views.home_html,
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
    re_path(
        "^swims/",
        include("illallangi.django.swimming.urls.swim"),
    ),
]
