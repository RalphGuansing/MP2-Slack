from django.contrib.auth.models import User
from django import forms
from .models import UserProfile
from django.contrib.auth import authenticate, login, logout, get_user_model

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ('username','password','first_name','last_name')
        labels = {
            'first_name': 'Name',
            'last_name': 'Degree Program/Office'
        }
        
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name','isStudent', 'degree_program_or_office', 'profile_picture')
        labels = {
            'isStudent': 'Are you a student?',
        }
        
class UserLoginForm(forms.Form):
    User = get_user_model()
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        user = authenticate(username=username, password=password)

        
        #user = User.objects.filter(username=username)
        #if user_qs.count()==1:
        #    user = user_qs.first()
        if username and password:
            user = authenticate(username=username, password= password)
            if not user:
                raise forms.ValidationError("This user does not exist")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect Password")
                
        return super(UserLoginForm, self).clean(*args, **kwargs)