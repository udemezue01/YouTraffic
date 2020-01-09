from django.db import models

# Create your models here.


class Hasghtag(models.Model):
	title 			 = models.CharField()


class Post(models.Model):

	User 			 = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)

	text 			 = models.CharField()
	image 			 = models.FileField()
	video 			 = models.FileField()

	hashtag 		 = models.ManyToManyField(Hashtag)

	created_at 		 = models.DateTimeField(auto_now_add = True)

