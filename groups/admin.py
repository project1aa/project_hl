from django.contrib import admin
from .models import (WhatsappGroup, TelegramGroup, SoroushGroup, EitaaGroup,
    IGapGroup, GapGroup)


admin.site.register(WhatsappGroup)
admin.site.register(TelegramGroup)
admin.site.register(SoroushGroup)
admin.site.register(EitaaGroup)
admin.site.register(IGapGroup)
admin.site.register(GapGroup)
