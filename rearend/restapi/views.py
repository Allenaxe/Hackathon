from django.contrib.auth.models import Group, User
from restapi.models import Course, Student
from rest_framework import permissions, viewsets
from rest_framework.response import Response
from restapi.serializers import GroupSerializer, UserSerializer, CourseSerializer, StudentSerializer


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
        user = User.objects.create(username = request.data.get('UserName'), email = request.data.get('Email'), password = request.data.get('Password'))
        Student.objects.create(UserName = user, Photo = request.data.get('Photo'), University = request.data.get('Department'), Age = request.data.get('Age'))
        return Response("ok")
    
    def update(self, request):
        user = User.objects.filter.update(username = request.data.get('UserName'), email = request.data.get('Email'), password = request.data.get('Password'))
        Student.objects.update(UserName = user, Photo = request.data.get('Photo'), University = request.data.get('Department'), Age = request.data.get('Age'))
        return Response("ok")

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