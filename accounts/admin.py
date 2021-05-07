from django.contrib import admin

# Register your models here.
from accounts.models import Blog, Profile

admin.site.register(Blog)
admin.site.register(Profile)
