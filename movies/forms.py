from django.forms import ModelForm
from django import forms
from movies.models import *

class Movieform(ModelForm):
	class Meta:
		model = Movies
		fields="__all__"