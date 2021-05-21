# Generated by Django 3.2 on 2021-05-21 06:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('created_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SNS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('github', models.URLField(blank=True)),
                ('blog', models.URLField(blank=True)),
                ('facebook', models.URLField(blank=True)),
                ('insta', models.URLField(blank=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'SNS',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_user', models.BooleanField(default=True)),
                ('korName', models.CharField(max_length=30, verbose_name='한글이름')),
                ('engName', models.CharField(max_length=30, verbose_name='영문이름')),
                ('address', models.CharField(max_length=50, verbose_name='주소')),
                ('email', models.EmailField(max_length=50, verbose_name='이메일')),
                ('phone', models.CharField(max_length=13, verbose_name='전화번호')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, upload_to='profile/images/user', verbose_name='프로필 사진')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='아이디')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_company', models.BooleanField(default=True)),
                ('phone', models.CharField(max_length=13, verbose_name='전화번호')),
                ('email', models.EmailField(max_length=50, verbose_name='이메일')),
                ('regiNum', models.IntegerField(verbose_name='사업자번호')),
                ('compName', models.CharField(max_length=30, verbose_name='기관명')),
                ('employee', models.ManyToManyField(blank=True, related_name='employer', to='accounts.Profile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='아이디')),
            ],
        ),
    ]
