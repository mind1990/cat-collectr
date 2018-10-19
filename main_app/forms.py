from django import forms
from .models import Cat


# class CatForm(forms.Form):
# 	name = forms.CharField(label='Name', max_length=100)
# 	breed = forms.CharField(label='Breed', max_length=100)
# 	description = forms.CharField(label='Description', max_length=250)
# 	age = forms.IntegerField(label='Age')


class CatForm(form.ModelForm):
	class Meta:
		model = Cat
		field = ('name', 'breed', 'description', 'age')




