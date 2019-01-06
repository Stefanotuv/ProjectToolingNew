from django import forms
from django.core import validators

#added a custom validator


class FormOne(forms.Form):

        app_name = forms.CharField(widget=forms.Textarea)
        app_type = forms.CharField()

        #like in the email we check that the app type is correct by re entering the value
        
        app_type_2 = forms.CharField(label = "re enter the app type")  
        app_id = forms.CharField()
        botcatcher = forms.CharField(required=False, widget = forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

        def clean(self):
                all_clean_data = super().clean()
                app_type = all_clean_data['app_type']
                app_type_2 = all_clean_data['app_type_2']

                if app_type != app_type_2:
                        raise forms.ValidationError("Does not match")