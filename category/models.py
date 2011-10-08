from django.db import models

class Type(models.Model):
	name = models.CharField(max_length = 30)
	zhcn = models.CharField(max_length = 50)

	def __unicode(self):
		return self.name

	class Meta:
		ordering = ['name']

class Article(models.Model):
	title = models.CharField(max_length = 150)
	date = models.DateField()
	author = models.CharField(max_length = 30)
	cont = models.CharField(max_length = 5000)
	parent_id = models.CharField(max_length = 5000)
	article_type = models.CharField(max_length = 30)

	def __unicode(self):
		return self.title

	class Meta:
		ordering = ['date']

class Replays(models.Model):
	name = models.CharField(max_length = 30)
	email = models.EmailField(blank = True)
	message = models.CharField(max_length = 5000)
	time = models.DateField()
	article_id = models.CharField(max_length = 5000)
	parent_id = models.CharField(max_length = 5000)

	def __unicode(self):
		return self.name

	class Meta:
		ordering = ['time']
	
class User(models.Model):
	username = models.CharField(max_length = 50)
	password = models.CharField(max_length = 18)

	def __unicode(self):
		return self.username

	class Meta:
		ordering = ['username']
