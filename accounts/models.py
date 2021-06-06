from datetime import datetime
from uuid import uuid4

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.urls import reverse



class Person(models.Model):
    is_user = models.BooleanField(default=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='지갑주소')

class Company(models.Model):
    is_company = models.BooleanField(default=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='지갑주소')

class Profile(models.Model):
    user_id = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name='아이디', db_column='user_id')
    korName = models.CharField(max_length=30, verbose_name='한글이름')
    engName = models.CharField(max_length=30, verbose_name='영문이름')
    email = models.EmailField(max_length=50, verbose_name='이메일')
    phone = models.CharField(max_length=13, verbose_name='전화번호')

    github = models.URLField(blank=True, verbose_name='깃허브')
    blog = models.URLField(blank=True, verbose_name='블로그')
    facebook = models.URLField(blank=True, verbose_name='페이스북')
    insta = models.URLField(blank=True,verbose_name='인스타')

    created_at = models.DateField(auto_now_add=True)
    # IPFS 네트워크를 사용하여 이미지 파일을 관리
    image_hash = models.CharField(max_length=255, blank=True, null=True)
    # image = models.ImageField(upload_to='profile/images/user', blank=True, verbose_name='프로필 사진')

    def get_absolute_url(self):
        return reverse('singlepage:page_detail', args=[self.id])

    def __str__(self):
        return f'{self.user_id.user}'

class SNS(models.Model):
    user_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    github = models.URLField(blank=True, verbose_name='깃허브')
    blog = models.URLField(blank=True, verbose_name='블로그')
    facebook = models.URLField(blank=True, verbose_name='페이스북')
    insta = models.URLField(blank=True,verbose_name='인스타')

    class Meta:
        verbose_name_plural = "SNS"

# class Company(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='아이디')
#     phone = models.CharField(max_length=13, verbose_name='전화번호')
#     email = models.EmailField(max_length=50, verbose_name='이메일')
#     regiNum = models.IntegerField(verbose_name='사업자번호')
#     compName = models.CharField(max_length=30, verbose_name='기관명')


def get_file_path(instance, filename):
    # 현재 날짜를 지정된 형식으로 포맷
    ymd_path = datetime.now().strftime('%Y/%m/%d')
    # 파일명을 고유한 문자열로 암호화하기 위해 사용
    uuid_name = uuid4().hex
    return '/'.join(['upload_file/',ymd_path,uuid_name])


upload_images = models.ImageField(upload_to=get_file_path, null=True, blank=True, verbose_name='프로필 사진')
filename = models.CharField(max_length=64, null=True, verbose_name='첨부파일명')


