from django.contrib import admin
from .models import User
from .forms import UserForm


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    form = UserForm
