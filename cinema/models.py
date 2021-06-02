from django.db import models


# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='', blank=True, null=True)
    cost = models.IntegerField(default=0, blank=True, null=True)
    date = models.DateField(blank=True, null=True)

    objects = models.Manager()

    class Meta:
        db_table = 'movies'

    def __str__(self):
        return self.name