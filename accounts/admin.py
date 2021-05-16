from django.contrib import admin

# Register your models here.
from accounts.models import Blog, Profile, SNS, Company

admin.site.register(Blog)
admin.site.register(Profile)
admin.site.register(Company)

class SnsAdmin(admin.ModelAdmin):
    list_display = ['user','github','blog','facebook','insta']
    raw_id_fields = ['user']
    list_filter = ['github']
    search_fields = ['github']


admin.site.register(SNS,SnsAdmin)