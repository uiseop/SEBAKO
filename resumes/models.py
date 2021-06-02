from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse

from accounts.models import Person


class SelfIntro(models.Model): # 간단자기소개서 작성 필드
    text = models.TextField(verbose_name='간단소개')
    # sns = models.JSONField(verbose_name='sns 종류 및 주소')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    user = models.ForeignKey(Person, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return f'[{self.user}] {self.text}'

class Experience(models.Model): # 경험 작성 필드
    title = models.CharField(max_length=30, verbose_name='직무')
    company = models.CharField(max_length=30, verbose_name='회사/장소')
    text = models.TextField(verbose_name='당시 한 일')
    dateFrom = models.DateField(verbose_name='시작일')
    dateEnd = models.DateField(verbose_name='종료일')

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    user = models.ForeignKey(Person, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return f'[{self.user}] {self.title}'

class Education(models.Model): # 학력 작성 필드
    school = models.CharField(max_length=30, verbose_name='학교명')
    major = models.CharField(max_length=30, verbose_name='전공명', null=True)
    # course = models.JSONField( verbose_name='이수과목')
    dateFrom = models.DateField(verbose_name='시작일')
    dateEnd = models.DateField(verbose_name='종료일')

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    user = models.ForeignKey(Person, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return f'[{self.user}] {self.school}'


class Resume(models.Model): # 자격증 작성 필드
    title = models.CharField(max_length=30, verbose_name='자격증명')
    regiNum = models.CharField(max_length=30, verbose_name='자격증번호')
    issure = models.CharField(max_length=30, verbose_name='발급처')
    dateAcq = models.DateField(verbose_name='취득일')
    file_hash = models.CharField(max_length=255, blank=True, null=True)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    user = models.ForeignKey(Person, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return f'[{self.user}] {self.title}'

    def get_absolute_url(self):
        return reverse('resumes:resume_detail', args=[self.id])

    class Meta:
        ordering = ['-created_at']

