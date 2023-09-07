from django.db import models

# Create your models here.
class personality(models.Model):
    Id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, null=False)
    gender = models.IntegerField(null=False) 
    age = models.IntegerField(null=False) 
    openness = models.IntegerField(null=False)
    neuroticism = models.IntegerField(null=False)
    conscientiousness = models.IntegerField(null=False)
    agreeableness = models.IntegerField(null=False)
    extraversion = models.IntegerField(null=False)
    result = models.CharField(max_length=20)

    def __str__(self):
        return [name,result]