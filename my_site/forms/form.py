from django import forms  
from .models import Login

class LoginForm(forms.Form):
    username = forms.CharField(max_length=20 , label='name')
    password = forms.CharField(max_length=20, label = 'password' , widget=forms.PasswordInput)
    #here username is key instead of name in forms.html


#third way is not bulit form from zoro and import it from module
#note it you want all field just write fields = '__all__'

class LoginForm3 (forms.ModelForm):
    class Meta:
        model = Login
        fields = ['username' , 'password']
