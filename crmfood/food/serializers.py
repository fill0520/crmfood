from rest_framework import serializers
from food.models import *


class TableSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Table
        fields = ('name',)

class RoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Role
        fields = ('name',)

class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Department
        fields = ('name',)

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'departmentid')

class StatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Status
        fields = ('name',)

class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Service
        fields = ('percentage',)



class UserSerializer(serializers.HyperlinkedModelSerializer):
    
	#roleid = serializers.StringRelatedField(many=False)

	class Meta:
		model = User
		fields = ('id', 'name', 'surname', 'login', 'password', 'email', 'roleid', 'dateofadd', 'phone')
	
class MealSerializer(serializers.HyperlinkedModelSerializer):
    
	#categoryid = serializers.StringRelatedField(many=False)

	class Meta:
		model = Meal
		fields = ('id', 'name', 'categoryid', 'price', 'description')
	

