from django.db import models
from taggit.managers import TaggableManager
from categories.models import Category


class Group(models.Model):
    TYPES = (
        ('iran', 'ایرانی'),
        ('foreign', 'خارجی'),
    )

    name = models.CharField(max_length=60)
    link = models.URLField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
        null=True)
    description = models.TextField()
    image = models.ImageField(upload_to='files/images/groups/')
    types = models.CharField(max_length=32, choices=TYPES)
    tags = TaggableManager()

    def __str__(self):
        return '{} ({})'.format(self.name, self.link)

    class Meta:
        abstract = True


class WhatsappGroup(Group):
    Group._meta.get_field('image').upload_to += 'whatsapp'

    class Meta:
        verbose_name_plural = 'Whatsapp Groups'


class TelegramGroup(Group):
    Group._meta.get_field('image').upload_to += 'telegram'

    class Meta:
        verbose_name_plural = 'Telegram Groups'


class SoroushGroup(Group):
    Group._meta.get_field('image').upload_to += 'soroush'


    class Meta:
        verbose_name_plural = 'Soroush Groups'


class EitaaGroup(Group):
    Group._meta.get_field('image').upload_to += 'eitaa'

    class Meta:
        verbose_name_plural = 'Eitaa Groups'


class IGapGroup(Group):
    Group._meta.get_field('image').upload_to += 'igap'

    class Meta:
        verbose_name_plural = 'IGap Groups'


class GapGroup(Group):
    Group._meta.get_field('image').upload_to += 'gap'

    class Meta:
        verbose_name_plural = 'Gap Groups'
