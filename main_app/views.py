from django.shortcuts import render, redirect
from django.http import HttpResponse

import json

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

from .forms import SignUpForm, NewRunForm, NewPokemonForm
from .models import Run, Pkinfo, Pokemon
from django.db.models import Q
default_rules = "Any Pokémon that faints is considered dead, and must be retired. The player may only catch the first wild Pokémon encountered in each area. If the first wild Pokémon encountered faints or flees, there are no second chances. This restriction does not apply to Pokémon able to be captured during static encounters, nor to Shiny Pokémon. The player must nickname all of their Pokémon, for the sake of forming stronger emotional bonds. The player may only use Pokémon they have captured themselves. As for trading and retrading the same Pokémon (for the purpose of evolving a Graveler, for example), there is no firm consensus. The player may not voluntarily reset and reload the game whenever things go wrong. Being able to do so would render all of the other rules pointless. Legendary and otherwise game-breaking pokemon may not be used."

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
    new_run = form.save(commit = False)
    new_run.user = request.user
    new_run.save()
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
  pokemon = Pkinfo.objects.get(id = pokemon_id)
  run = Run.objects.get(id = run_id)
  pokemon_form = NewPokemonForm(initial={
    'status': "Alive", 
    'name': pokemon.name, 
    'pk_id': pokemon.pk_id, 
    'type_1': pokemon.type_1, 
    'type_2': pokemon.type_1, 
    'picture': pokemon.picture, 
    'hp': pokemon.hp, 
    'attack': pokemon.attack, 
    'defense': pokemon.defense, 
    'sp_attack': pokemon.sp_attack, 
    'sp_defense': pokemon.sp_defense, 
    'speed': pokemon.speed,
    })
  return render(request, 'profile/new_pokemon.html', {'pokemon': pokemon, 'run': run, 'pokemon_form': pokemon_form})
  
#Define Add Pokemon View
@login_required
def add_pokemon(request, run_id, pokemon_id):
  form = NewPokemonForm(request.POST or None)
  if request.POST and form.is_valid():
    new_pokemon = form.save(commit = False)
    new_pokemon.run_id = run_id
    new_pokemon.save()
    return redirect('show_run', run_id = run_id)
  else:
    return redirect('profile')

  pokemon = Pkinfo.objects.get(id = pokemon_id)
  run = Run.objects.get(id = run_id)
  return render(request, 'profile/new_pokemon.html', {'pokemon': pokemon, 'run': run})

@login_required
def delete_pokemon (request, run_id, pokemon_id):
    pokemon = Pokemon.objects.get(id = pokemon_id)
    pokemon.delete()
    return redirect ('show_run', run_id = run_id)

#Define New Pokemon View
@login_required
def search_results(request, run_id):
  run = Run.objects.get(id = run_id)
  query = request.GET['q']
  pokemon = Pkinfo.objects.filter(
      Q(name__icontains=query) | Q(type_1__icontains=query) | Q(type_2__icontains=query)
  )
  return render(request, 'profile/search_results.html', {'pokemon': pokemon, 'run': run})