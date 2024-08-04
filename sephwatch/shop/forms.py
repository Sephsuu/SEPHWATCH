from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(
        label='',
        widget = forms.EmailInput(attrs={
            'type': 'email', 
            'placeholder': 'E-mail Address',
            'class': 'mail_text',
        })
    )
    password = forms.EmailField(
        label='',
        widget = forms.PasswordInput(attrs={
            'type': 'password', 
            'placeholder': 'Password',
            'class': 'mail_text',
        })
    )