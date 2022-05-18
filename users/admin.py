from django.contrib import admin
from .models import Profile

# Enable CRUD operations on Profile model from admin page.

admin.site.register(Profile)
