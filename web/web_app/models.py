from django.db import models

# Create your models here.
 
class StatusModel(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        #return self.name
        return f'{self.name} - {self.id}'

class Album(models.Model):
    title=models.CharField(max_length=100)
    artist=models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
class Song(models.Model):
    title=models.CharField(max_length=100)
    album=models.ForeignKey(Album,on_delete=models.CASCADE)

    def __str__(self):
        return self.title