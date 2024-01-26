from django.contrib.auth.models import Group, User
from restapi.models import Course
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['UserName', 'Photo', 'University', 'Age', 'Skill', 'Learned', 'Score']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'CourceName', 'University', 'DifficultyLevel', 'CourseRating', 'CourseDescription']