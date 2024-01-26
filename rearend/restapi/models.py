from django.db import models
from django.contrib.auth.models import User

class Cource(models.Model):
  CourceName = models.CharField(max_length = 100)
  University = models.CharField(max_length = 100)
  DifficultyLevel = models.CharField(max_length = 100)
  CourseRating = models.FloatField()
  CourseDescription = models.TextField()
'''
class Student(models.Model):
  UserName = models.OneToOneField(User, on_delete = models.CASCADE)
  University = models.CharField(max_length = 100)
  Age = models.IntegerField()
  Skill = models.TextField()
'''
# Create your models here.