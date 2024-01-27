from django.contrib.auth.models import Group, User
from django.contrib import auth
from restapi.models import Course, Student
from rest_framework import permissions, viewsets
from rest_framework.response import Response
from restapi.serializers import GroupSerializer, UserSerializer, CourseSerializer, StudentSerializer
from rest_framework.decorators import action
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import HttpResponse
import json


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request)
        if serializer.is_valid():
            serializer.save()

class StudentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request):
        try:
            User.objects.get(username = request.data.get('UserName'))
            return Response("failed")
        except:
            user = User.objects.create(username = request.data.get('UserName'), email = request.data.get('Email'))
            user.set_password(request.data.get('Password'))
            user.save()
            Student.objects.create(UserName = user, Photo = request.data.get('Photo'), University = request.data.get('Department'), Age = request.data.get('Age'))
            return Response("ok")
    
    def update(self, request):
        user = User.objects.filter.update(username = request.data.get('UserName'), email = request.data.get('Email'), password = request.data.get('Password'))
        Student.objects.update(UserName = user, Photo = request.data.get('Photo'), University = request.data.get('Department'), Age = request.data.get('Age'))
        return Response("ok")
    
    @action(methods = ['get'], detail = False) 
    def printUser(self, request):
        return Response(Student.objects.get(UserName = User.objects.get(username = request.user)).Photo)

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.AllowAny]

class CourseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.AllowAny]

@csrf_exempt
def login(request):
    if request.user.is_authenticated:
        return HttpResponse('ok')
    data = json.loads(request.body)
    username = data['username']
    password = data['password']
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
        print(request.user)
        return HttpResponse('ok')
    else:
        return HttpResponse('failed')