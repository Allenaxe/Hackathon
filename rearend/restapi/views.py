from django.contrib.auth.models import Group, User
from restapi.models import Cource
from rest_framework import permissions, viewsets

from restapi.serializers import GroupSerializer, UserSerializer, CourseSerializer


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
    queryset = Cource.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.AllowAny]