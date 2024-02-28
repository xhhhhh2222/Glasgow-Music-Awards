from django.shortcuts import render

def index(request):
    response = render(request, 'glasgowMusicAwards/index.html')
    return response

def about(request):
    response = render(request, 'glasgowMusicAwards/about.html')
    return response

def login(request):
    response = render(request, 'glasgowMusicAwards/login.html')
    return response

def logout(request):
    response = render(request, 'glasgowMusicAwards/logout.html')
    return response

def addArtist(request):
    response = render(request, 'glasgowMusicAwards/add-artist.html')
    return response

def artistList(request):
    response = render(request, 'glasgowMusicAwards/artist-list.html')
    return response

def register(request):
    response = render(request, 'glasgowMusicAwards/register.html')
    return response

def genres(request):
    response = render(request, 'glasgowMusicAwards/genres.html')
    return response

def artistPage(request):
    response = render(request, 'glasgowMusicAwards/artist-page.html')
    return response