from django.urls import path
from .views import IndexView, SpidermanView, CaptainAmericaView, NarutoView

urlpatterns = [
    path('', IndexView.as_view()),
    path('spiderman', SpidermanView.as_view()),
    path('capamerica', CaptainAmericaView.as_view()),
    path('naruto', NarutoView.as_view()),
]
