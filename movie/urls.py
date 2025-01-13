"""
movie.urls
"""

from django.urls import path
from . import views

app_name="movie"
urlpatterns = [
    path('',views.movie_view,name="movie"),
    path('<int:pk>/',views.movie_detail,name="detail"),

    # api end points 
    # path('api-auth/', include('rest_framework.urls'))
    path('api/movie/list/',views.movie_list_api,name="movie_list_api"),
    path('api/movie/list/<pk>/',views.movie_detail_api,name="movie_detail_api"),
    path('api/movie/create/',views.movie_create_api,name="movie_create_api"),
    path('api/movie/update/<pk>/',views.movie_update_api,name="movie_update_api"),
    path('api/movie/delete/<pk>/',views.movie_delete_api,name="movie_delete_api"),

    


]


