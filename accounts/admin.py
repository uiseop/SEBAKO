from django.contrib import admin

# Register your models here.
from accounts.models import Blog, Profile, Resume

admin.site.register(Blog)
admin.site.register(Profile)
admin.site.register(Resume)