from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('accounts/signup/', views.signup, name='signup'),
  path('profile/', views.profile, name='profile'),
  path('run/<int:run_id>/', views.show_run, name='show_run'),
  path('new_run/', views.new_run, name='new_run'),
  path('add_run/', views.add_run, name='add_run'),
]