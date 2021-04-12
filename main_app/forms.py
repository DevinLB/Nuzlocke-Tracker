from django import forms
from .models import Run
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
    rules = forms.CharField(
        max_length=5000, 
        required=True, 
        widget=forms.Textarea(attrs={'class': 'form-control'}, 
        ))
    class Meta:
        model = Run
        fields = ['name', 'game', 'rules']