from django import forms


class StudentForm(forms.Form):
    name = forms.CharField(label="Name", max_length="100")
    email = forms.EmailField(label="Email", max_length="100")
    password = forms.CharField(label="Password", max_length="100", widget=forms.PasswordInput)
