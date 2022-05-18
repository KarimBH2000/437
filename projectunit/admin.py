from django.contrib import admin
from .models import Post

# Enable admin CRUD operations on Posts.

admin.site.register(Post)
