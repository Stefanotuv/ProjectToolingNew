from django import forms
from django.core import validators

#added a custom validator
def check_length_of_3(value):
    if len(value) <2:
        raise forms.ValidationError("error, too short")

class FormOne(forms.Form):
    app_name = forms.CharField(widget=forms.Textarea)
    app_type = forms.CharField()
    app_id = forms.CharField(validators=[check_length_of_3])
    botcatcher = forms.CharField(required=False, widget = forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])
