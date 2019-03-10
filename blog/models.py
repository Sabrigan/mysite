from django.db import models


class Timestamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(Timestamp):
    title = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return self.title
