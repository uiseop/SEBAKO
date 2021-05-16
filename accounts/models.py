from datetime import datetime
from uuid import uuid4

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.urls import reverse


class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return f'[{self.id}] {self.title}'

    def summary(self):
        return self.body[:100]

class Profile(models.Model):
    is_user = models.BooleanField(default=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='아이디')
    korName = models.CharField(max_length=30, verbose_name='한글이름')
    engName = models.CharField(max_length=30, verbose_name='영문이름')
    address = models.CharField(max_length=50, verbose_name='주소')
    email = models.EmailField(max_length=50, verbose_name='이메일')
    phone = models.CharField(max_length=13, verbose_name='전화번호')

    created_at = models.DateField(auto_now_add=True)

    image = models.ImageField(upload_to='profile/images/user', blank=True, verbose_name='프로필 사진')

    def get_absolute_url(self):
        return reverse('singlepage:page_detail', args=[self.id])

    def __str__(self):
        return f'{self.user}'

class SNS(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    github = models.URLField(null=True, blank=True)
    blog = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    insta = models.URLField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "SNS"

class Company(models.Model):
    is_company = models.BooleanField(default=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='아이디')
    phone = models.CharField(max_length=13, verbose_name='전화번호')
    email = models.EmailField(max_length=50, verbose_name='이메일')
    regiNum = models.IntegerField(verbose_name='사업자번호')
    compName = models.CharField(max_length=30, verbose_name='기관명')

    employee = models.ManyToManyField('Profile', blank=True, related_name='employer')


def get_file_path(instance, filename):
    # 현재 날짜를 지정된 형식으로 포맷
    ymd_path = datetime.now().strftime('%Y/%m/%d')
    # 파일명을 고유한 문자열로 암호화하기 위해 사용
    uuid_name = uuid4().hex
    return '/'.join(['upload_file/',ymd_path,uuid_name])


upload_images = models.ImageField(upload_to=get_file_path, null=True, blank=True, verbose_name='프로필 사진')
filename = models.CharField(max_length=64, null=True, verbose_name='첨부파일명')


