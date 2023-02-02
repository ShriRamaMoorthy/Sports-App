from email.policy import default
from django.db import models

# Create your models here.
class Players(models.Model):
    first_name = models.CharField(max_length=100,null=True)
    last_name = models.CharField(max_length=100,null=True)
    club=models.CharField(max_length=100,null=True)
    nation =  models.CharField(max_length=100,null=True)
    pace=models.IntegerField(default=0)
    dribbling=models.IntegerField(default=0)
    shooting = models.IntegerField(default=0)
    defending = models.IntegerField(default=0)
    passing=models.IntegerField(default=0)
    physical=models.IntegerField(default=0)


    def __str__(self):
        return "%s %s %s" %(self.first_name, self.last_name, self.club)