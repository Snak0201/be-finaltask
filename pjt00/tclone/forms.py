from django import forms
from django.contrib.auth import get_user_model

# class FollowForm(forms.Form):
#     user = forms.CharField()
#     def clean_user(self):
#         user = self.cleaned_data['user']
#         return user

class FollowXForm(forms.Form):
    user = forms.CharField()
    def clean_user(self):
        user = self.cleaned_data['user']
        return user
