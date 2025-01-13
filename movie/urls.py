"""
movie.urls
"""

from django.urls import path
from . import views

app_name="movie"
urlpatterns = [
    path('',views.movie_view,name="movie"),
    path('<int:pk>/',views.movie_detail,name="detail"),


]


