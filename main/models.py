from django.db import models

class Animal(models.Model):
    name = models.CharField(max_length=100, null=False)
    species = models.CharField(max_length=100, null=False)
    age = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
