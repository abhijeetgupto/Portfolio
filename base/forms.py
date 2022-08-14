from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'input-field'}))
    subject = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'input-field'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'input-field'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'input-field'}))
