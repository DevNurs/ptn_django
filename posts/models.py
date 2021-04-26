from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='post_imag')
    description = models.TextField()

    def __str__(self):
        return self.title



