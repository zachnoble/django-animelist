from django.urls import path

from . import views

app_name = 'animelist'
urlpatterns = [
    path('', views.index, name='index'),
    path('anime/<int:anime_id>/details', views.anime, name='anime'),
    path('users/<int:user_id>/details', views.user, name='user'),
]
