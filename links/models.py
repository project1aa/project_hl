from django.db import models
from taggit.managers import TaggableManager
import os
from urllib.parse import urlparse


def site_image_path(instance, filename):
    ext = os.path.splitext(filename)[-1] # filename extension
    ext_domain = urlparse(instance.link).netloc # domain name
    if ext_domain.startswith('www.'):
        ext_domain = ext_domain[4:]
    new_filename = '{}{}'.format(ext_domain, ext) # filename: domain + extension
    return 'files/images/sites/{}'.format(new_filename)

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
    image = models.ImageField(upload_to=site_image_path)
    types = models.CharField(max_length=32, choices=TYPES)
    tags = TaggableManager()

    def __str__(self):
        return '{} - ({})'.format(self.name, self.link)


class Channel(models.Model):
    TYPES = (
        ('iran', 'ایرانی'),
        ('foreign', 'خارجی'),
    )

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
        return '{} - ({})'.format(self.name, self.channel_id)

    class Meta:
        abstract = True


class TelegramChannel(Channel):
    Channel._meta.get_field('image').upload_to += 'telegram'


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
