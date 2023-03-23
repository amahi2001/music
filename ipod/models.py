from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey

# musicians


class Musician(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    # this function allows us to see the name of the musician in our admin page
    def __str__(self):
        return self.first_name + " " + self.last_name

    @classmethod
    def create(cls, **kwargs):
        first_name = kwargs['first_name']

# albums - ForeignKey to Musician


class Album(models.Model):
    artist = ForeignKey(Musician, on_delete=CASCADE)
    title = models.CharField(max_length=200)

    # this function allows us to see the title of the album in our admin page
    def __str__(self):
        return self.title
