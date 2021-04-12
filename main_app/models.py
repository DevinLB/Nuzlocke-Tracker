from django.db import models
from django.urls import reverse
from datetime import date
from django.db.models import JSONField

# Import the User
from django.contrib.auth.models import User

# Create your models here.

class Run(models.Model):
  name = models.CharField(max_length=100)
  game = models.CharField(max_length=100)
  rules = models.CharField(max_length=1000)

  user = models.ForeignKey(User, on_delete=models.CASCADE)
  def __str__(self):
    return self.name

class Pkinfo(models.Model):
  name = models.CharField(max_length=100)
  pk_id = models.CharField(max_length=100)
  jfield = JSONField()

  def __str__(self):
    return self.name

class Pokemon(models.Model):
  name = models.CharField(max_length=100)
  nickname = models.CharField(max_length=100)
  pk_id = models.CharField(max_length=100)
  status = models.CharField(max_length=15, null=True)
  type_1 = models.CharField(max_length=15)
  type_2 = models.CharField(max_length=15, null=True)

  run = models.ForeignKey(Run, on_delete=models.CASCADE)
  def __str__(self):
    return self.name


# class Pkinfo(models.Model):
#   name = models.CharField(max_length=100)
#   pk_id = models.CharField(max_length=100)
#   type_1 = models.CharField(max_length=15)
#   type_2 = models.CharField(max_length=15, null=True)
  
  # def __str__(self):
  #   return self.name


# class Game(models.Model):
#   name = models.CharField(max_length=100)
#   generation = models.CharField(max_length=100)
#   areas = models.CharField(max_length=1000)
#   pokedex = models.CharField(max_length=1000)

#   def __str__(self):
#     return self.name