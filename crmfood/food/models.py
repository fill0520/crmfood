from django.db import models

# Create your models here.

class Table(models.Model):
	name = models.CharField(max_length=50)
	def __str__(self):
		return self.name

class Role(models.Model):
	name = models.CharField(max_length=50)
	def __str__(self):
		return self.name

class Department(models.Model):
	name = models.CharField(max_length=50)
	def __str__(self):
		return self.name

class Category(models.Model):
	name = models.CharField(max_length=50)
	departmentid = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='categories')
	def __str__(self):
		return self.name

class Status(models.Model):
	name = models.CharField(max_length=50)
	def __str__(self):
		return self.name

class Service(models.Model):
	percentage = models.IntegerField(max_length=50)
	def __str__(self):
		return self.percentage

class User(models.Model):
	roleid = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='users')
	name = models.CharField(max_length=200)
	surname = models.CharField(max_length=200)
	login = models.CharField(max_length=200)
	password = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	dateofadd = models.CharField(max_length=200)
	phone = models.CharField(max_length=200)
	def __str__(self):
		return self.name

class Meal(models.Model):
	categoryid = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='users')
	name = models.CharField(max_length=200)
	description = models.CharField(max_length=200)
	price = models.IntegerField(max_length=50)
	def __str__(self):
		return self.name