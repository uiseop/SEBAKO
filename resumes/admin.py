from django.contrib import admin

# Register your models here.
from resumes.models import Resume



class ResumeAdmin(admin.ModelAdmin):
    list_display = ['id','user','title','dateAcq']
    raw_id_fields = ['user']
    list_filter = ['created_at','updated_at','user']
    search_fields = ['title'] # ForeginKey 필드는 적용 불가
    ordering = ['id']

admin.site.register(Resume, ResumeAdmin)