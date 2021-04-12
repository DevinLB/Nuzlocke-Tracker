from django.shortcuts import render, redirect
from django.http import HttpResponse

import json

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

from .forms import SignUpForm, NewRunForm
from .models import Run, Pkinfo, Pokemon
from django.db.models import Q
default_rules = "Any Pokémon that faints is considered dead, and must be released or put in the Pokémon Storage System permanently (or may be transferred to another game, as long as the Pokémon is never able to be used again during this run). The player may only catch the first wild Pokémon encountered in each area, and none else. If the first wild Pokémon encountered faints or flees, there are no second chances. If the first encounter in the area is a double battle, the player is free to choose which of the two wild Pokémon they would like to catch but may only catch one of them. This restriction does not apply to Pokémon able to be captured during static encounters, nor to Shiny Pokémon. The player must nickname all of their Pokémon, for the sake of forming stronger emotional bonds. The player may only use Pokémon they have captured themselves, meaning Pokémon acquired through trading, Mystery Gifts, etc., are prohibited. As for trading and retrading the same Pokémon (for the purpose of evolving a Graveler, for example), there is no firm consensus. As of White: Hard-Mode Episode 3, it is implied that the player can accept Pokémon that are received freely from NPCs. The player may not voluntarily reset and reload the game whenever things go wrong. Being able to do so would render all of the other rules pointless. Legendary and otherwise game-breaking pokemon may not be used."

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
  run_form = NewRunForm(initial={'rules': default_rules});
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
    return redirect('profile')

# Define Show Pokemon View
@login_required
def show_pokemon(request, pokemon_id):
  pokemon = Pkinfo.objects.get(id = pokemon_id)
  return render(request, 'profile/show_pokemon.html', {'pokemon': pokemon})
  
#Define New Pokemon View
@login_required
def new_pokemon(request, run_id, pokemon_id):
  pokemon = Pokemon.objects.get(id = pokemon_id)
  run = Run.objects.get(id = run_id)
  return render(request, 'profile/new_pokemon.html', {'pokemon': pokemon, 'run': run})
  
#Define Add Pokemon View
@login_required
def new_pokemon(request, run_id, pokemon_id):
  pokemon = Pokemon.objects.get(id = pokemon_id)
  run = Run.objects.get(id = run_id)
  return render(request, 'profile/new_pokemon.html', {'pokemon': pokemon, 'run': run})

#Define New Pokemon View
@login_required
def search_results(request, run_id):
  run = Run.objects.get(id = run_id)
  query = request.GET['q']
  pokemon = Pkinfo.objects.filter(
      Q(name__icontains=query) | Q(type_1__icontains=query) | Q(type_2__icontains=query)
  )
  return render(request, 'profile/search_results.html', {'pokemon': pokemon, 'run': run})