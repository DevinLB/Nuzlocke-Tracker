from django import forms
from .models import Run, Pokemon, Pkinfo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

GAMES = [
    ('platinum', 'Platinum'),
    ('diamond', 'Diamond'),
    ('pearl', 'Pearl'),
]

class SignUpForm(UserCreationForm):
    current_city = forms.CharField(max_length=100)
    class Meta: 
        model = User
        fields = ['username', 'email']

class NewRunForm(forms.ModelForm):
    name = forms.CharField(max_length=100, required=True)
    game = forms.CharField(label='Game', widget=forms.RadioSelect(choices=GAMES, attrs={'class': ''}))
    rules = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'form-control'}, ))
    class Meta:
        model = Run
        fields = ['name', 'game', 'rules']

class NewPokemonForm(forms.ModelForm):
    nickname = forms.CharField(max_length=100, required=True)
    status = forms.CharField(max_length=15, widget=forms.HiddenInput())
    name = forms.CharField(max_length=100, widget=forms.HiddenInput())
    pk_id = forms.CharField(max_length=100, widget=forms.HiddenInput())
    type_1 = forms.CharField(max_length=15, widget=forms.HiddenInput())
    type_2 = forms.CharField(max_length=15, widget=forms.HiddenInput())
    picture = forms.CharField(max_length=100, widget=forms.HiddenInput())
    hp = forms.IntegerField(widget=forms.HiddenInput())
    attack = forms.IntegerField(widget=forms.HiddenInput())
    defense = forms.IntegerField(widget=forms.HiddenInput())
    sp_attack = forms.IntegerField(widget=forms.HiddenInput())
    sp_defense = forms.IntegerField(widget=forms.HiddenInput())
    speed = forms.IntegerField(widget=forms.HiddenInput())
    
    class Meta:
        model = Pokemon
        fields = ['nickname', 'status', 'name', 'pk_id', 'type_1', 'type_2', 'picture', 'hp', 'attack', 'defense', 'sp_attack', 'sp_defense', 'speed']