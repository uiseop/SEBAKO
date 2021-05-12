from django.contrib import admin

# Register your models here.
from resumes.models import Resume, SelfIntro, Experience, Education

class EducationAdmin(admin.ModelAdmin):
    list_display = ['user', 'school','major']
    raw_id_fields = ['user']
    list_filter = ['created_at']
    search_fields = ['school','major']

class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['user', 'company', 'title']
    raw_id_fields = ['user']
    list_filter = ['created_at']
    search_fields = ['company','title']

class SelfIntroAdmin(admin.ModelAdmin):
    list_display = ['user', 'text','created_at']
    raw_id_fields = ['user']
    list_filter = ['created_at']

admin.site.register(SelfIntro,SelfIntroAdmin)
admin.site.register(Experience,ExperienceAdmin)
admin.site.register(Education,EducationAdmin)


class ResumeAdmin(admin.ModelAdmin):
    list_display = ['id','user','title','dateAcq']
    raw_id_fields = ['user']
    list_filter = ['created_at','updated_at','user']
    search_fields = ['title'] # ForeginKey 필드는 적용 불가
    ordering = ['id']

admin.site.register(Resume, ResumeAdmin)