from django.db import models

# Create your models here.
class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500)
    content = models.TextField()
    author = models.CharField(max_length=250)
    slug = models.CharField(max_length=250)
    views = models.IntegerField(default=0)
    timeStamp = models.DateTimeField(blank=True)


    def __str__(self):
        return self.title + 'By - '+ self.author