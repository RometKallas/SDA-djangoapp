
from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic.edit import CreateView

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin

from viewer.models import Movie
from django.views import View
from django.views.generic import FormView, ListView, UpdateView, DeleteView, DetailView
from viewer.forms import MovieForm, GenreForm

from logging import getLogger
from django.urls import reverse_lazy

LOGGER = getLogger()

# Create your views here.
def hello2(request, s):
    return HttpResponse(f"Hello {s} world")

def hello(request, s0):
  s1 = request.GET.get('s1', '')
  return render(
    request, template_name='viewer/hello.html',
    context={'adjectives': [s0, s1, 'beautiful', 'wonderful']}
  )

def movies(request):
  return render(
    request, template_name='viewer/movies.html',
    context={'movies': Movie.objects.all()}
  )


class MoviesView(View):
  def get(self, request):
    return render(
      request, template_name='viewer/movies.html',
      context={'movies': Movie.objects.all()}
    )

# class MovieCreateView(FormView):

#   template_name = 'viewer/form.html'
#   form_class = MovieForm
#   success_url = reverse_lazy('movie_create')

#   def form_valid(self, form):
#     result = super().form_valid(form)
#     cleaned_data = form.cleaned_data
#     Movie.objects.create(
#       title=cleaned_data['title'],
#       genre=cleaned_data['genre'],
#       rating=cleaned_data['rating'],
#       released=cleaned_data['released'],
#       description=cleaned_data['description']
#     )
#     return result

#   def form_invalid(self, form):
#     LOGGER.warning('User provided invalid data.')
#     return super().form_invalid(form)

class StaffRequiredMixin(UserPassesTestMixin):
  def test_func(self):
    return self.request.user.is_staff

class MovieCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
  
  template_name = 'viewer/form.html'
  form_class = MovieForm
  success_url = reverse_lazy('movies')
  permission_required = 'viewer.add_movie'
  
  def form_invalid(self, form):
    LOGGER.warning('User provided invalid data.')
    return super().form_invalid(form)

class GenreCreateView(CreateView):
  
  template_name = 'viewer/form.html'
  form_class = GenreForm
  success_url = reverse_lazy('movies')
  
  def form_invalid(self, form):
    LOGGER.warning('User provided invalid data.')
    return super().form_invalid(form)

class MovieUpdateView(StaffRequiredMixin, PermissionRequiredMixin, UpdateView):

  template_name = 'viewer/form.html'
  model = Movie
  form_class = MovieForm
  success_url = reverse_lazy('movies')
  permission_required = 'viewer.change_movie'

  def form_invalid(self, form):
    LOGGER.warning('User provided invalid data while updating a movie.')
    return super().form_invalid(form)

class MovieDeleteView(StaffRequiredMixin, PermissionRequiredMixin, DeleteView):
  template_name ="viewer/delete_movie.html"
  model = Movie
  success_url = reverse_lazy('movies')
  permission_required = 'viewer.delete_movie'

  def test_func(self):
    return super().test_func() and self.request.user.is_superuser

class MovieDetailView(DetailView):
  template_name = "viewer/movie_detail.html"
  model = Movie