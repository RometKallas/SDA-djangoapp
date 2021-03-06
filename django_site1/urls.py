"""django_site1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

from viewer.models import Genre, Movie

from viewer.views import MoviesView, MovieCreateView, hello, movies, GenreCreateView, MovieUpdateView, MovieDeleteView, MovieDetailView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/<s0>', hello, name="hello"),
    #This is based on a function
    path('', movies, name="movies"),
    path('movie/create', MovieCreateView.as_view(), name='movie_create'),
    path('viewer/new_genre', GenreCreateView.as_view(), name='new_genre'),
    path('movie/update/<pk>', MovieUpdateView.as_view(), name='movie_update'),
    path('movie/delete/<pk>', MovieDeleteView.as_view(), name='movie_delete'),
    path('movie/view/<pk>', MovieDetailView.as_view(), name='movie_view'),
    #This is based on a class template
    #path('', MoviesView.as_view(), name="movies"),

    path('accounts/', include('accounts.urls', namespace='accounts'))


]
