from django.urls import path, include
from awards import views
from django.contrib import admin

app_name = 'awards'

urlpatterns = [
    path('', views.index, name='index'),
    path('awards/', include('awards.urls')),
    path('admin/', admin.site.urls),
]