from django.contrib import admin
from .models import * #importing all models

admin.site.register(Musician)
admin.site.register(Album)

# Register your models here.
