from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return f'[{self.id}] {self.title}'

    def summary(self):
        return self.body[:100]

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='아이디')
    korName = models.CharField(max_length=30, verbose_name='한글이름')
    engName = models.CharField(max_length=30, verbose_name='영문이름')
    address = models.CharField(max_length=50, verbose_name='주소')
    email = models.EmailField(max_length=50, verbose_name='이메일')
    phone = models.CharField(max_length=13, verbose_name='전화번호')

    created_at = models.DateField(auto_now_add=True)

    AddSNS = models.ManyToManyField('SNS', blank=True, related_name='domain')

    def __str__(self):
        return f'{self.user}'

class SNS(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    url = models.URLField("Site URL")

    class Meta:
        verbose_name_plural = "SNS"

