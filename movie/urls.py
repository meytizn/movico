"""
movie.urls
"""

from django.urls import path,include
from . import views
from rest_framework import routers


router=routers.SimpleRouter()
# router.register('movie',views.Movie_viewset)  # function based executed 
router.register('genre',views.Genre_viewset)
router.register('actor',views.Actor_viewset)
router.register('link',views.Link_viewset)
router.register('comment',views.Comment_viewset)

app_name="movie"

urlpatterns = [
    path('',views.movie_view,name="movie"),
    path('movie/<int:pk>/',views.movie_detail,name="detail"),

    #Api endPoints

    # class base api view used by viewsets and routers 
    path('api/', include(router.urls)),

    # funcation base api view used by decorator 
    path('api/movie/',views.movie_list_api,name="movie_list_api"),
    path('api/movie/create/',views.movie_create_api,name="movie_create_api"),
    path('api/movie/update/<pk>/',views.movie_update_api,name="movie_update_api"),
    path('api/movie/delete/<pk>/',views.movie_delete_api,name="movie_delete_api"),
    path('api/movie/<pk>/',views.movie_detail_api,name="movie_detail_api"),

    


]


