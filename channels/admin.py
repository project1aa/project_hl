from django.contrib import admin
from .models import (TelegramChannel, SoroushChannel, EitaaChannel,
    IGapChannel, GapChannel)


admin.site.register(TelegramChannel)
admin.site.register(SoroushChannel)
admin.site.register(EitaaChannel)
admin.site.register(IGapChannel)
admin.site.register(GapChannel)
