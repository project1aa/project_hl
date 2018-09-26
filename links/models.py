from django.db import models
from taggit.managers import TaggableManager


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
        return '{} - ({})'.format(self.name, self.url)


class Category(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name
