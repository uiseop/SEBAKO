from django.contrib import admin

# Register your models here.
from accounts.models import Profile, SNS, Company, Person


class ProfileAdim(admin.ModelAdmin):
    list_display = ['user_id','korName']

admin.site.register(Profile,ProfileAdim)
admin.site.register(Company)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['id','user']

admin.site.register(Person,PersonAdmin)

class SnsAdmin(admin.ModelAdmin):
    list_display = ['user_id','github','blog','facebook','insta']
    raw_id_fields = ['user_id']
    list_filter = ['github']
    search_fields = ['github']


admin.site.register(SNS,SnsAdmin)