from django import forms

class LoginForm(forms.Form):
    nome_login = forms.CharField(label='Nome de Login', required=True, max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control',
            'placeholder': 'Ex.: João Silva'}
        ))
    senha = forms.CharField(label='Senha', required=True, max_length=70, widget=forms.PasswordInput(
        attrs={'class': 'form-control',
            'placeholder': 'Digite sua senha'}
        ))

class RegistroForm(forms.Form):
    nome_cadastro = forms.CharField(label='Nome', required=True, max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control',
            'placeholder': 'Ex.: João Silva'}
        ))

    email = forms.EmailField(label='Email', required=True, max_length=100, widget=forms.EmailInput(
        attrs={'class': 'form-control',
            'placeholder': 'Ex.: joaosilva@gmail.com'}
            ))

    senha_1 = forms.CharField(label='Senha', required=True, max_length=70, widget=forms.PasswordInput(
        attrs={'class': 'form-control',
            'placeholder': 'Digite sua senha'}
        ))   

    senha_2 = forms.CharField(label='Confirmar senha', required=True, max_length=70, widget=forms.PasswordInput(
    attrs={'class': 'form-control',
        'placeholder': 'Digite sua senha novamente '}
    ))  