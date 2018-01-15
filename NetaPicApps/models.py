from django.db import models
import uuid

class Image(models.Model):
    uuid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    tags = models.CharField(max_length = 255, )
    image = models.ImageField(upload_to = "images/")