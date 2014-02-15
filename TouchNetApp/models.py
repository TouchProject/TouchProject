# coding=utf-8

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta

class Utilisateur(models.Model):
	pseudo = models.CharField(max_length=50)
	mot_de_passe = models.CharField(max_length=50)
	nom = models.CharField(max_length=50)
	prenom = models.CharField(max_length=50)
	mail = models.CharField(max_length=50)
	telephone = models.CharField(max_length=10)
	langue = models.CharField(max_length=50)
	pays = models.CharField(max_length=50)
	biographie = models.CharField(max_length=160)
	localisation = models.CharField(max_length=100)
	date = models.DateTimeField()

	def __unicode__(self):
		return self.pseudo

class Touch(models.Model):
	texte = models.CharField(max_length=160)
	date_touch = models.DateTimeField(auto_now_add=True, editable=False)
	utilisateur = models.ForeignKey(Utilisateur)