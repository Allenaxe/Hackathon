from django.contrib.auth.models import Group, User
from restapi.models import Course, Student
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'password', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'UserName', 'Photo', 'University', 'Age', 'Skill', 'Learned', 'Score']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'CourceName', 'University', 'DifficultyLevel', 'CourseRating', 'CourseDescription']