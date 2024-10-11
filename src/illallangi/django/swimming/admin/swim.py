from django.contrib.admin import ModelAdmin, register

from illallangi.django.swimming.models import Swim


@register(Swim)
class SwimModelAdmin(ModelAdmin):
    pass
