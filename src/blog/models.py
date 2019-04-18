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


# class PostTimeline(Timestamp):
#     y_begin = models.IntegerField()
#     m_begin = models.IntegerField()
#     d_begin = models.IntegerField()
#     t_begin = models.TimeField()
#     y_end = models.IntegerField()
#     m_end = models.IntegerField()
#     d_end = models.IntegerField()
#     t_end = models.TimeField()
#     headline = models.CharField(max_length=500)
#     body = models.TextField()
#     media = models.URLField()
#     media_credit = models.CharField(max_length=250)
#     # media_caption =
#     # media_thumbnail =
#     type_tl = models.CharField()
#     group = models.CharField()
#     background = models.CharField()
