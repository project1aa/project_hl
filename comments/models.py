from django.db import models


class Comment(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    text = models.TextField()
    published = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date',)
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.name
