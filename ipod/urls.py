from django.contrib import admin
from django.urls import path
from . import views

app_name = 'albums'

urlpatterns = [
    path('', views.musician_view, name = "ipod"),

    #album paths; delete, add, edit
    path("delete-album/<pk>/", views.delete_album, name = "delete_album"),
    path("add-album/", views.add_album_form, name = "add_album"),
    path("edit-album/<pk>/", views.AlbumUpdateView.as_view(), name = "edit_album"),
    
    #musician paths; delete, add, edit
    path("delete-musician/<pk>", views.delete_musician, name = "delete_musician"),
    path("add-musician/",views.add_musician_form, name = "add_musician"),
    path("edit-musician/<pk>/", views.edit_musician_form, name = "edit_musician"),
]