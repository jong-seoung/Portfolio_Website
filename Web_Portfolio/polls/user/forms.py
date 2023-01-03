from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import User
from polls.content.models import Project
from datetime import datetime
from django.utils.dateformat import DateFormat
today = DateFormat(datetime.now()).format('Y-m-d')

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email',)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.profile_img = "default_profile.png"
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password',
                'is_active', 'is_admin')

    def clean_password(self):
        return self.initial["password"]

#  프로젝트

class ProjectCreationForm(forms.ModelForm):
    project_name = forms.CharField(label='project_name',)

    class Meta:
        model = Project
        fields = ('email',)

    def clean_project(self):
        project_name = self.cleaned_data.get(label='project_name',)
        return project_name

    def save(self, commit=True):
        project = super().save(commit=False)
        project.project_name(self.cleaned_data["project_name"])
        if commit:
            project.save()
        return project

class ProjectChangeForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ('email', 'content', 'image', 'project_name', 'url_blog', 'url_github')

    def clean_project(self):
        return self.initial["project"]