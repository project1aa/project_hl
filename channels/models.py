from django.db import models
from taggit.managers import TaggableManager
from categories.models import Category
import re


class Channel(models.Model):
    TYPES = (
        ('iran', 'ایرانی'),
        ('foreign', 'خارجی'),
    )

    name = models.CharField(max_length=60)
    channel_id = models.CharField(max_length=32) # channel's id
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
        null=True)
    description = models.TextField()
    image = models.ImageField(upload_to='files/images/channels/')
    types = models.CharField(max_length=32, choices=TYPES)
    tags = TaggableManager()

    def __str__(self):
        return '{} ({})'.format(self.name, self.channel_id)

    class Meta:
        abstract = True


class TelegramChannel(Channel):
    Channel._meta.get_field('image').upload_to += 'telegram'

    def clean(self):
        comp = re.compile(r'^([a-zA-Z]+)([\w\d]*)([a-zA-Z0-9]+)$')
        if not comp.search(self.channel_id):
            raise ValidationError({'channel_id':
                _('Sorry, this name is invalid.')})

        if len(self.channel_id) < 5:
            raise ValidationError({'channel_id':
                _('Channel names must have at least 5 characters')})

    class Meta:
        verbose_name_plural = 'Telegram Channels'


class SoroushChannel(Channel):
    Channel._meta.get_field('image').upload_to += 'soroush'

    class Meta:
        verbose_name_plural = 'Soroush Channels'

    def clean(self):
        comp = re.compile(r'^([\w\d\.]+)$')
        if not comp.search(self.channel_id):
            raise ValidationError({'channel_id':
                _('Sorry, this name is invalid.')})

        if len(self.channel_id) < 6:
            raise ValidationError({'channel_id':
                _('Channel names must have at least 6 characters')})


class EitaaChannel(Channel):
    Channel._meta.get_field('image').upload_to += 'eitaa'

    class Meta:
        verbose_name_plural = 'Eitaa Channels'

    def clean(self):
        comp = re.compile(r'^([a-zA-Z]+)([\w\d]*)([a-zA-Z0-9]+)$')
        if not comp.search(self.channel_id):
            raise ValidationError({'channel_id':
                _('Sorry, this name is invalid.')})

        if len(self.channel_id) < 6:
            raise ValidationError({'channel_id':
                _('Channel names must have at least 6 characters')})


class IGapChannel(Channel):
    Channel._meta.get_field('image').upload_to += 'igap'

    class Meta:
        verbose_name_plural = 'IGap Channels'

    def clean(self):
        comp = re.compile(r'^([a-zA-Z]+)([\w\d]*)([a-zA-Z0-9]+)$')
        if not comp.search(self.channel_id):
            raise ValidationError({'channel_id':
                _('Sorry, this name is invalid.')})

        if len(self.channel_id) < 5:
            raise ValidationError({'channel_id':
                _('Channel names must have at least 5 characters')})


class GapChannel(Channel):
    Channel._meta.get_field('image').upload_to += 'gap'

    class Meta:
        verbose_name_plural = 'Gap Channels'

    def clean(self):
        comp = re.compile(r'^([a-zA-Z0-9]+)([\w\d]*)([a-zA-Z0-9]+)$')
        if not comp.search(self.channel_id):
            raise ValidationError({'channel_id':
                _('Sorry, this name is invalid.')})

        if len(self.channel_id) < 4:
            raise ValidationError({'channel_id':
                _('Channel names must have at least 4 characters')})
