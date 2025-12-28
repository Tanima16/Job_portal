from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import USER_TYPE_CHOICES, Job

User = get_user_model()

class UserRegistrationForm(UserCreationForm):
    display_name = forms.CharField(max_length=50, required=True, help_text='First Name')
    email = forms.EmailField(required=True)
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES, required=True)

    class Meta:
        model = User
        fields = ['username', 'display_name', 'email', 'user_type']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['display_name']
        user.email = self.cleaned_data['email']
        user.user_type = self.cleaned_data['user_type']
        if commit:
            user.save()
        return user

class LoginForm(AuthenticationForm):
    pass

class RecruiterProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['company_name']
        
class JobSeekerProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['skills', 'resume']

class JobPostForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'number_of_openings', 'category', 'description', 'skills_required']
