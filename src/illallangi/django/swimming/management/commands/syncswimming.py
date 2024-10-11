from django.core.management.base import BaseCommand

from illallangi.django.swimming.adapters import SwimmingAdapter as DjangoSwimmingAdapter
from illallangi.mastodon.adapters import SwimmingAdapter as MastodonSwimmingAdapter


class Command(BaseCommand):
    help = "Sync Swimming data from one adapter to another."
    requires_migrations_checks = True

    def handle(
        self,
        *_args: tuple,
        **_kwargs: dict,
    ) -> None:
        src = MastodonSwimmingAdapter()
        dst = DjangoSwimmingAdapter()

        src.load()
        dst.load()

        src.sync_to(dst)

        self.stdout.write(
            self.style.SUCCESS(
                "Successfully synchronised.",
            ),
        )
