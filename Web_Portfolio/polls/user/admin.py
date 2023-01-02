from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserChangeForm, UserCreationForm, ProjectChangeForm, ProjectCreationForm
from .models import User
from polls.content.models import Project


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'date_of_birth', 'is_admin','is_active','profile_img','name','nickname',)
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('date_of_birth','profile_img','name','nickname',)}),
        ('Permissions', {'fields': ('is_admin',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','name','nickname', 'password1', 'password2')}
        ),
    )   
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

# 프로젝트
class ProjectAdmin(admin.ModelAdmin):
    form = ProjectChangeForm
    add_form = ProjectCreationForm

    list_display = ('project_name','email',)
    list_filter = ('project_name',)
    fieldsets = (
        ('content', {'fields': ('project_name','content',)}),
        ('Writer', {'fields': ('email',)}),
        ('Url', {'fields': ('image','url_blog', 'url_github')}),
    )   

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'content', 'image', 'project_name', 'url_blog', 'url_github')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(User, UserAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.unregister(Group)