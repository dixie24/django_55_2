from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=150)
    password1 = forms.CharField(required=True)
    password2 = forms.CharField(required=True)
    
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 != password2:
            raise forms.ValidationError("Passwords do not match")


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput)