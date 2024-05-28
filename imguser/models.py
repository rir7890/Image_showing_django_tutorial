from django.db import models

# Create your models here.


class MyModel(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name
