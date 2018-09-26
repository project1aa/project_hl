from django.contrib import admin
from .models import (Category, Site, TelegramChannel, SoroushChannel,
    IGapChannel, GapChannel, EitaaChannel)


admin.site.register(Category)
admin.site.register(Site)
admin.site.register(TelegramChannel)
admin.site.register(SoroushChannel)
