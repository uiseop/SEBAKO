from django.contrib import admin

# Register your models here.
from accounts.models import Blog, Profile, SNS

admin.site.register(Blog)
admin.site.register(Profile)

class SnsAdmin(admin.ModelAdmin):
    list_display = ['user_id','name','url']
    raw_id_fields = ['user_id']
    list_filter = ['user_id']
    search_fields = ['name']


admin.site.register(SNS,SnsAdmin)