from django.db import models



class Timestamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True



class Post(Timestamp):
    title = models.CharField(max_length=255)
    body = models.TextField()
    test = models.BooleanField(default=False)
    date_de_debut = models.DateTimeField(auto_now=False)
    date_de_fin = models.DateTimeField(auto_now_add=False)
    url_test = models.URLField(default="www.pierre-dauphin.hopto.org")
    image = models.ImageField(default="{%static img/fond1.jpg %}")


    def __str__(self):
        return self.title

# data = serializers.serialize("xml", Post.objects.all())
# XMLSerializer = serializers.get_serializer("xml")
# xml_serializer = XMLSerializer()
# xml_serializer.serialize('xml', Post.objects.all(), fields=('title','body'))
# data = xml_serializer.getvalue()
# with open("file.xml", "w") as out:
#     xml_serializer.serialize(Post.objects.all(), stream=out)