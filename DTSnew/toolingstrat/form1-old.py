from django import forms
from django.core import validators


class FormOne(forms.Form):
    app_name = forms.CharField(widget=forms.Textarea)
    app_type = forms.CharField()
    app_id = forms.CharField()
    botcatcher = forms.CharField(required=False, widget = forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])




 """"   
    def clean_botcatcher(self):
        botcatcher = self.cleaned_data['botcatcher']
        if len(botcatcher) > 0:

            raise forms.ValidationError("error!")
        return botcatcher
"""
