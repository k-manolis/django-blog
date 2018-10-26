from django.db import models

# Create your models here.
class Article(models.Model):
	title = models.CharField(max_length=100)
	slug  = models.SlugField()
	body  = models.TextField()
	date  = models.DateTimeField(auto_now_add=True) # automatically populate this field with datetime
	# add in thumnail later
	# add in author later

	## to migrate file you have to user 2 python commands
	## python manage.py makemigrations
	## python manage.py migrate

	##Article.objects.all()

	def __str__(self):
		return self.title


	def snippet(self):
		return self.body[:50] + '...'