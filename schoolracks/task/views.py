from rest_framework import routers, serializers, viewsets, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializer import UserSerializer, RackSerializer, StudentSerializer
from .models import Racks, Student
from rest_framework import filters

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RackViewSet(viewsets.ModelViewSet):
    queryset = Racks.objects.all()
    serializer_class = RackSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['student_id']
