# coding=utf-8

from django.contrib import admin
from TouchNetApp.models import Utilisateur, Touch

class TouchInline(admin.TabularInline):
	model = Touch

class UtilisateurAdmin(admin.ModelAdmin):
	fieldsets = [
				 ('Profil', {
				  'fields': ['pseudo', 'nom', 'prenom', 'date']
				  }),
				 ('Information', {
				  'fields': ['mail', 'telephone', 'pays', 'langue', 'biographie']
				  }),
				 ('Confidentiel', {
				  'fields': ['mot_de_passe'],
				  'classes': ['collapse']
				  }),
				 ]
	list_display = ('nom', 'prenom', 'pseudo', 'mail', 'pays', 'date');
	list_filter = ['date']
	ordering = ('nom', 'prenom')
	search_fields = ['nom']
	inlines = [TouchInline]

class TouchAdmin(admin.ModelAdmin):
	list_display = ('date_touch', 'utilisateur', 'texte');
	list_filter = ['date_touch']
	ordering = ['date_touch']
	search_fields = ['texte']

# Register your models here.
admin.site.register(Utilisateur, UtilisateurAdmin)
admin.site.register(Touch, TouchAdmin)

