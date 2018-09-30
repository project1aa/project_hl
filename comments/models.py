from django.db import models


class Comment(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    text = models.TextField()
    published = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.name
