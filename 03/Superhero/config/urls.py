from django.urls import path
from django.urls.conf import include


urlpatterns = [
    path('', include('hero.urls')),
    path('naruto', include('hero.urls')),
]
