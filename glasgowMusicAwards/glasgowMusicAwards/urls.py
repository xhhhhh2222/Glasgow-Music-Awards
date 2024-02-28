from django.urls import path, include
from awards import views

app_name = 'awards'

urlpatterns = [
    path('', views.index, name='index'),
    path('awards/', include('awards.urls')),
]