# Generated by Django 3.2 on 2021-05-21 05:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('resumes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Single',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resumes.education')),
                ('exper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resumes.experience')),
                ('resum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resumes.resume')),
                ('selfIntro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resumes.selfintro')),
            ],
        ),
    ]
