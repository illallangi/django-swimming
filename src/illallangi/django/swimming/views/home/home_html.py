from django.core.paginator import Paginator
from django.http import HttpRequest
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.http import require_GET

from illallangi.django.swimming.models.swim import Swim


@require_GET
def home_html(
    request: HttpRequest,
    **_: dict,
) -> render:
    base_template = "partial.html" if request.htmx else "base.html"

    return render(
        request,
        "swimming/home.html",
        {
            "base_template": base_template,
            "page": Paginator(
                object_list=[
                    {
                        "name": "Swims",
                        "description": "View all swims.",
                        "a": {
                            "href": reverse("swimming:swims_html"),
                            "text": f"View { Swim.objects.count() } Swims",
                        },
                        "img": {
                            "src": "swimming/swims.png",
                            "alt": "Swims",
                        },
                    },
                ],
                per_page=10,
            ).get_page(
                request.GET.get("page", 1),
            ),
            "breadcrumbs": [
                {
                    "title": "Swimming",
                    "url": reverse(
                        "swimming:home_html",
                    ),
                },
            ],
            "links": [
                {
                    "rel": "alternate",
                    "type": "text/html",
                    "href": request.build_absolute_uri(
                        reverse(
                            "swimming:home_html",
                        ),
                    ),
                },
            ],
        },
    )
