from django.db import models

# from django_snacks.snacks_project import snacks

# Create your models here.
class Snacks(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.title