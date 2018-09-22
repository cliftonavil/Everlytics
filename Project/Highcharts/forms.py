from django import forms
from .import models


class CreateBrowsers(forms.ModelForm):
    Users = forms.IntegerField(label='', widget=forms.TextInput(attrs={'size': 15, 'placeholder': 'Users Count'}))
    class Meta:
        model = models.Browsers
        fields = ['Browsers', 'Users']

