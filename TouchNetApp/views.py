# coding=utf-8

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from TouchNetApp.models import Utilisateur, Touch
import datetime

# Page d'accueil, affiche des touchs de tout les utilisateurs
def index(request):
	utilisateur = get_object_or_404(Utilisateur, pk = 1) # Une fois la mise en sesisonopé, utilisé request.SESSION['pk']
	touchs = Touch.objects.all().order_by('date_touch')
	contexte = { 'touchs': touchs, 'utilisateur': utilisateur,}
	return render(request, 'index.html', contexte)

# Affichage des touch correspondant à l'utilisateur selectionné
def profile(request, utilisateur_id):
	utilisateur = get_object_or_404(Utilisateur, pk = utilisateur_id)
	touchs = utilisateur.touch_set.all()
	contexte = { 'utilisateur': utilisateur, 'touchs': touchs,}
	return render(request, 'profile.html', contexte)