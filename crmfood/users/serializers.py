from .models import *
from rest_framework import serializers



class UserSerializer(serializers.ModelSerializer):
    #first_name = serializers.CharField(read_only=True, source="user.first_name")
    #last_name = serializers.CharField(read_only=True, source="user.last_name")

    class Meta:
        model = User
        fields = ('id', 'name', 'password')