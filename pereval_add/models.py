from django.db import models


class Users(models.Model):
    emails = models.EmailField(unique=True)
    fam = models.CharField(max_length=30)
    nam = models.CharField(max_length=30)
    otc = models.CharField(max_length=30, null=True)


class Coords(models.Model):
    latitude = models.FloatField(null=True, blank=True, default=None)
    longitude = models.FloatField(null=True, blank=True, default=None)
    height = models.IntegerField(null=True, blank=True, default=None)


class Level(models.Model):
    winter = models.CharField(max_length=2)
    spring = models.CharField(max_length=2)
    summer = models.CharField(max_length=2)
    autumn = models.CharField(max_length=2)


class Pereval_image(models.Model):
    image = models.ImageField(upload_to='media/', null=True, blank=True)


class Pereval_added(models.Model):
    users = models.ForeignKey(Users, on_delete=models.CASCADE)
    beautyTitle = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    other_titles = models.CharField(max_length=30)
    connect = models.TextField()
    add_time = models.DateTimeField(auto_now_add=True)
    coords = models.ForeignKey(Coords, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)