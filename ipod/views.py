from django.shortcuts import redirect, render
from .models import Musician, Album
# from django.http import HttpResponse
from django.views.generic.edit import UpdateView
from .forms import *


def musician_view(request):
    # musician_entry = Musician(first_name = "Abrar", last_name = "Mahi")
    # musician_entry.save()
    # album_entry = Album(artist = musician_entry,  title = "Interning at NYPL - Django Rocks!")
    # album_entry.save()
    get_musicianList = Musician.objects.all()
    albums = Album.objects.all()
    context = {'albums': albums, 'musicians': get_musicianList}
    return render(request, 'ipod/home.html', context)


def album_view(request):
    get_album = Album.objects.all()
    context = {'albums': get_album}
    return render(request, 'ipod/album.html', context)

# Create your views here.


def delete_album(request, pk):
    album = Album.objects.filter(pk=pk)
    if request.method == 'GET':
        album.delete()
        return redirect("/")  # redirects to the empty path ' '
    return render(request, 'ipod/home.html', {'albums': album})


# class AlbumFormView(CreateView):
#     template_name = 'ipod/add_album.html'
#     model = Album
#     fields = ['artist', 'title']
#     success_url = '/'

########### alternative way to add album #############

def add_album_form(request, *args, **kwargs):

    context = {'form': AlbumForm}
    if (request.method == "GET"):
        return render(request, 'ipod/add_album.html', context)

    if (request.method == "POST"):
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request, 'ipod/add_album.html', context)


class AlbumUpdateView(UpdateView):
    model = Album
    fields = ('__all__')
    template_name = 'ipod/edit_album.html'
    success_url = '/'

########### alternative way to edit album ##############
# def edit_album_form(request, pk):
#     album = Album.objects.get(pk=pk)
#     form = AlbumForm(instance=album)
#     context = {'form': form}
#     if (request.method == "GET"):
#         return render(request, 'ipod/edit_album.html', context)
#     if (request.method == "POST"):
#         form = AlbumForm(request.POST, instance=album)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#         else:
#             return render(request, 'ipod/edit_album.html', context)


def delete_musician(request, pk):
    musician = Musician.objects.filter(pk=pk)
    if request.method == 'GET':
        musician.delete()
        return redirect("/")  # redirects to the empty path ' '
    return render(request, 'ipod/home.html', {'musicians': musician})


def add_musician_form(request):
    context = {'form': MusicianForm}
    if (request.method == "GET"):
        return render(request, 'ipod/add_musician.html', context)

    if (request.method == "POST"):
        form = MusicianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request, 'ipod/add_musician.html', context)

# edit musician form with error message


def edit_musician_form(request, pk):
    musician = Musician.objects.get(pk=pk)
    form = MusicianForm(instance=musician)
    context = {'form': form}
    if (request.method == "GET"):
        return render(request, 'ipod/edit_musician.html', context)

    if (request.method == "POST"):
        form = MusicianForm(request.POST, instance=musician)
        if form.is_valid():
            form.save()
            return redirect('/')
        form.save()
        return redirect('/')
    else:
        return render(request, 'ipod/edit_musician.html', context)
