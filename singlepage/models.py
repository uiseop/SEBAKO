from django.db import models

# Create your models here.
from resumes.models import SelfIntro, Experience, Education, Resume


class Single(models.Model):
    selfIntro = models.ForeignKey(SelfIntro, on_delete=models.CASCADE)
    exper = models.ForeignKey(Experience, on_delete=models.CASCADE)
    edu = models.ForeignKey(Education, on_delete=models.CASCADE)
    resum = models.ForeignKey(Resume, on_delete=models.CASCADE)

