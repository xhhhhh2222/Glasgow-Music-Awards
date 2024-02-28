from django.urls import path
from awards import views

app_name = 'awards'

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('login/', views.login, name="login"),
    path("register/", views.register, name="register"),
    path("genres/", views.genres, name="genres"),
    path("genres/<slug:genre_name_slug>/artist-list/", 
         views.artistList, name="artist-list"),
    path("genres/<slug:genre_name_slug>/artist-list/<slug:artist_name_slug>/artist-page/",
        views.artistPage, name="artist-page"),
    path("add-artist/", views.addArtist, name="add-artist"),
    path("logout/", views.logout, name="logout")
]
