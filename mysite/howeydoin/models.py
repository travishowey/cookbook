from django.db import models

# Create your models here.

class Recipe(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=200)
    ingredients = models.CharField(max_length=2000)
    instructions = models.CharField(max_length=2000)
    details = models.CharField(max_length=2000, default="it's a good recipe, really")
    image = models.ImageField(upload_to='pictures', default='https://www.google.com/url?sa=i&url=https%3A%2F%2Funsplash.com%2Fs%2Fphotos%2Fplate&psig=AOvVaw0MX3G1sCt7ND-FBIXv69ZM&ust=1650592695338000&source=images&cd=vfe&ved=0CAwQjRxqFwoTCLj3mYuHpPcCFQAAAAAdAAAAABAD')
