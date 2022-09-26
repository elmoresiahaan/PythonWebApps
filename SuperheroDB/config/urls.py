"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from hero.views import PhotoDetailView, PhotoListView, LuffyView, NarutoView, SaitamaView, TanjiroView, NatsuView
from django.views.generic import RedirectView
from django.contrib.admin import site
from django.contrib import admin
from django.urls import path
'''
urlpatterns = [
    path('admin/', admin.site.urls),
]


urlpatterns = [
    path(r'admin/', site.urls),
]
'''

urlpatterns = [

    # admin
    path(r'admin/', site.urls),

    # Home
    path('', RedirectView.as_view(url='photo/')),

    # Photos
    path('photo/', PhotoListView.as_view()),
    path('photo/<int:id>', PhotoDetailView.as_view()),
    path('photo/luffy', LuffyView.as_view()),
    path('photo/naruto', NarutoView.as_view()),
    path('photo/saitama', SaitamaView.as_view()),
    path('photo/tanjiro', TanjiroView.as_view()),
    path('photo/natsu', NatsuView.as_view()),
]
