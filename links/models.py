from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from taggit.managers import TaggableManager
from urllib.parse import urlparse
import os
import re


class Site(models.Model):
    TYPES = (
        ('iran', 'ایرانی'),
        ('foreign', 'خارجی'),
    )

    name = models.CharField(max_length=60)
    link = models.URLField()
    category = models.ForeignKey('Category', on_delete=models.SET_NULL,
        null=True)
    description = models.TextField()
    created = models.PositiveSmallIntegerField(default=0, blank=True)
    image = models.ImageField(upload_to='files/images/sites/')
    types = models.CharField(max_length=32, choices=TYPES)
    tags = TaggableManager()

    def __str__(self):
        return '{} - ({})'.format(self.name, self.link)


class Channel(models.Model):
    TYPES = (
        ('iran', 'ایرانی'),
        ('foreign', 'خارجی'),
    )

    # '(\w)+(\w\d_)+'

    name = models.CharField(max_length=60)
    channel_id = models.CharField(max_length=32) # channel's id
    category = models.ForeignKey('Category', on_delete=models.SET_NULL,
        null=True)
    description = models.TextField()
    created = models.PositiveSmallIntegerField(default=0, blank=True)
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


class SoroushChannel(Channel):
    Channel._meta.get_field('image').upload_to += 'soroush'


class EitaaChannel(Channel):
    Channel._meta.get_field('image').upload_to += 'eitaa'


class IGapChannel(Channel):
    Channel._meta.get_field('image').upload_to += 'igap'


class GapChannel(Channel):
    Channel._meta.get_field('image').upload_to += 'gap'


class Category(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Group(models.Model):
    TYPES = (
        ('iran', 'ایرانی'),
        ('foreign', 'خارجی'),
    )

    name = models.CharField(max_length=60)
    link = models.URLField()
    category = models.ForeignKey('Category', on_delete=models.SET_NULL,
        null=True)
    description = models.TextField()
    created = models.PositiveSmallIntegerField(default=0, blank=True)
    image = models.ImageField(upload_to='files/images/groups/')
    types = models.CharField(max_length=32, choices=TYPES)
    tags = TaggableManager()

    def __str__(self):
        return '{} - ({})'.format(self.name, self.link)


class WhatsappGroup(Group):
    Channel._meta.get_field('image').upload_to += 'whatsapp'


class TelegramGroup(Group):
    Channel._meta.get_field('image').upload_to += 'telegram'


class SoroushGroup(Group):
    Channel._meta.get_field('image').upload_to += 'soroush'


class EitaaGroup(Group):
    Channel._meta.get_field('image').upload_to += 'eitaa'


class IGapGroup(Group):
    Channel._meta.get_field('image').upload_to += 'igap'


class GapGroup(Group):
    Channel._meta.get_field('image').upload_to += 'gap'
