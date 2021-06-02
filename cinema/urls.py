from django.urls import path

from cinema import views

urlpatterns = [
    path('movie-view/<int:id>/view', views.movie_view, name='movie-view'),
    path('movie-detail/<int:id>/edit', views.movie_detail, name='movie-detail'),
    path('index/', views.index, name='index'),
    path('movie-delete/<int:id>/delete', views.movie_delete, name='movie-delete'),
    path('movie-new/', views.movie_new, name='movie-new'),
    path('movie-save/', views.movie_save, name='movie-save'),
]
