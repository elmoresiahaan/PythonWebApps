from django.views.generic import RedirectView
from django.urls import path

from photos.views import PhotoDetailView, PhotoListView, LuffyView, NarutoView, SaitamaView, TanjiroView, NatsuView


urlpatterns = [

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
