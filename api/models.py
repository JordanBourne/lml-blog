from django.db import models

class Topic(models.Model):
    subject = models.CharField(max_length=100)

class Post(models.Model):
    post_content = models.CharField(max_length=20000)
    post_title = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

class TopicPreReq(models.Model):
    subject_id = models.IntegerField(default=0)
    prereq_id = models.IntegerField(default=0)
