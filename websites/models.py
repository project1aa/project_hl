from django.db import models
from taggit.managers import TaggableManager
from categories.models import Category


class Website(models.Model):
    TYPES = (
        ('iran', 'ایرانی'),
        ('foreign', 'خارجی'),
    )

    name = models.CharField(max_length=60)
    link = models.URLField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
        null=True)
    description = models.TextField()
    image = models.ImageField(upload_to='files/images/sites/')
    types = models.CharField(max_length=32, choices=TYPES)
    tags = TaggableManager()

    def __str__(self):
        return '{} - ({})'.format(self.name, self.link)
