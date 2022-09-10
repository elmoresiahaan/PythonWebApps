from django.urls import path
from .views import IndexView, IchigoView, LuffyView, NarutoView

urlpatterns = [
    path('', IndexView.as_view()),
    path('ichigo', IchigoView.as_view()),
    path('luffy', LuffyView.as_view()),
    path('naruto', NarutoView.as_view()),
]
