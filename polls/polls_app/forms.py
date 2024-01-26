# polls_app/forms.py
from django import forms

class UserResponseForm(forms.ModelForm):
    class Meta:
        model = UserResponse
        fields = ['poll', 'choice', 'user_id', 'email']
