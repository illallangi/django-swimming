from typing import ClassVar

import diffsync

from illallangi.django.swimming.diffsyncmodels import Swim
from illallangi.django.swimming.models import Swim as DjangoSwim


class SwimmingAdapter(diffsync.Adapter):
    Swim = Swim

    top_level: ClassVar = [
        "Swim",
    ]

    type = "django_swimming"

    def load(
        self,
    ) -> None:
        for obj in DjangoSwim.objects.all():
            self.add(
                Swim(
                    pk=obj.pk,
                    url=obj.url,
                    date=obj.date,
                    distance=obj.distance,
                    laps=obj.laps,
                ),
            )
