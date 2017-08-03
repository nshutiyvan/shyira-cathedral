from  django import forms

class ContactForm(forms.Form):
    firstname =forms.CharField(max_length=120,initial='none')
    lastname = forms.CharField(max_length=120,initial='none')
    email = forms.CharField(max_length=120,initial='none-reply@gmail.com')
    message = forms.CharField(max_length=400)
class Album(forms.Form):
    name=forms.CharField(max_length=120)