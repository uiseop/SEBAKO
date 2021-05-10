from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Resume(models.Model):
    title = models.CharField(max_length=30, verbose_name='자격증명')
    regiNum = models.CharField(max_length=30, verbose_name='자격증번호')
    issure = models.CharField(max_length=30, verbose_name='발급처')
    dateAcq = models.DateField()

    file_upload = models.FileField(upload_to='resumes/files/%Y/%m/%d', blank=True)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'[{self.user}] {self.title}'