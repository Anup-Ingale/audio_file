from django.db import models

# Create your models here.

# Songs Model
class Song(models.Model):
    #  fields : id,name,duration,upload_time
    name        = models.CharField(max_length=200)
    duration    = models.IntegerField(default=0)
    upload_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Podcast Model
class Podcast(models.Model):
    #  fields : id,name,duration,uploaded time, host, participant.
    name                = models.CharField(max_length=200)
    duration_in_sec     = models.IntegerField()
    upload_time         = models.DateTimeField(auto_now=True)
    host                = models.CharField(max_length=150)

# Audiobook Model
class Audiobook(models.Model):
    # fields : id ,title , author of title, narrator , duration in sec , uploaded time
    title            = models.CharField(max_length=200)
    author_of_title  = models.CharField(max_length=200)
    narrator         = models.CharField(max_length=200)
    duration_in_sec  = models.IntegerField(default=0)
    uploaded_time    = models.DateTimeField(auto_now=True)

