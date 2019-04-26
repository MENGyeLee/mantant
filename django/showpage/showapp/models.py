from django.db import models

# Create your models here.
class Test1(models.Model):
    name = models.CharField(max_length=20)


class movie(models.Model):
    content = models.CharField(max_length=4000)
    objects=models.Manager()





class weathers(models.Model):

    wCity=models.CharField(max_length=16)

    wDate=models.CharField(max_length=16)

    wWeather=models.CharField(max_length=64)

    wTemp=models.CharField(max_length=32)

    objects=models.Manager()





class phones(models.Model):

    mNo=models.CharField(max_length=32)

    mMark=models.CharField(max_length=256)

    mPrice=models.CharField(max_length=32)

    mNote=models.CharField(max_length=1024)

    mFile=models.CharField(max_length=256)

    objects=models.Manager()



class shubao(models.Model):

    Price=models.CharField(max_length=32)

    Title=models.CharField(max_length=256)

    objects=models.Manager()