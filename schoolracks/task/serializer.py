from rest_framework import serializers

from django.contrib.auth.models import User
from .models import Student, Racks

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'password')


class RackSerializer(serializers.ModelSerializer):

    class Meta:
        ordering = ['-id']
        model = Racks
        fields = ("id", "racks_id", "students")
        extra_kwargs = {'students': {'required': False}}


class StudentSerializer(serializers.ModelSerializer):
    racks = RackSerializer(many = True, read_only = True)

    class Meta:
        ordering = ['-id']
        model = Student
        fields = ("id", "student_id", "racks")
        extra_kwargs = {'racks': {'required': False}}
