from django.urls import path
from .views import MovieView, MovieDetail

urlpatterns = [
    path('', MovieView.as_view(), name='home'),
    path('detail/<slug:slug>', MovieDetail.as_view(), name='detail_movie')
]
