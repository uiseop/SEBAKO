# Generated by Django 3.2 on 2021-06-07 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumes', '0002_resume_signature'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='domain',
            field=models.URLField(blank=True, verbose_name='이더넷'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='signature',
            field=models.CharField(blank=True, max_length=10, verbose_name='인증'),
        ),
    ]
