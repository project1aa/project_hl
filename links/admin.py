from django.contrib import admin
from . import models


admin.site.register(models.Category)

# sites
admin.site.register(models.Site)

# channels
admin.site.register(models.TelegramChannel)
admin.site.register(models.SoroushChannel)
admin.site.register(models.EitaaChannel)
admin.site.register(models.IGapChannel)
admin.site.register(models.GapChannel)

# groups
admin.site.register(models.WhatsappGroup)
admin.site.register(models.TelegramGroup)
admin.site.register(models.SoroushGroup)
admin.site.register(models.EitaaGroup)
admin.site.register(models.IGapGroup)
admin.site.register(models.GapGroup)
