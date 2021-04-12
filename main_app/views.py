from django.shortcuts import render, redirect
from django.http import HttpResponse

import json

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

from .forms import SignUpForm, NewRunForm
from .models import Run, Pkinfo, Pokemon


### VIEWS

# Define Signup View
def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A GET or a bad POST request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

# Define Home View 
def home(request):
    return render(request, 'index.html')

# Define Profile View
@login_required
def profile(request):
  profile = request.user
  runs = profile.run_set.all()
  return render(request, 'profile/profile.html', {'profile': profile, 'runs': runs})

# Define Show Run View
@login_required
def show_run(request, run_id):
  run = Run.objects.get(id = run_id)
  pokemon = run.pokemon_set.all()
  
  print(pokemon)
  print(run)
  content = {
    'run': run,
    'pokemon': pokemon,
  }
  return render(request, 'profile/show_run.html', content)

# Define New Run View
@login_required
def new_run(request):
  run_form = NewRunForm();
  return render(request, 'profile/new_run.html', {'run_form': run_form})

# Define Add Run View
@login_required
def add_run(request):
  form = NewRunForm(request.POST or None)
  if request.POST and form.is_valid():
    new_review = form.save(commit = False)
    new_review.user = request.user
    new_review.save()
    return redirect('profile')
  else:
    return render(request, 'profile/new_run.html')

# Define Show Pokemon View
@login_required
def show_pokemon(request, pokemon_id):
  pokemon = Pokemon.objects.get(id = pokemon_id)
  return render(request, 'profile/show_pokemon.html', {'pokemon': pokemon})
  