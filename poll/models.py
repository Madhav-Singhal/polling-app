from django.db import models

# Create your models here.
class PollModel(models.Model):

    title = models.TextField()
    c1 = models.CharField(max_length = 100)
    c2 = models.CharField(max_length = 100)
    c3 = models.CharField(max_length = 100)
    count1 = models.IntegerField(default = 0)
    count2 = models.IntegerField(default = 0)
    count3 = models.IntegerField(default = 0)



    def __unicode__(self):
        return self.id