from django import forms

class AddBook(forms.Form):
    titel = forms.CharField(widget=forms.TextInput())
    author = forms.CharField(widget=forms.TextInput())
