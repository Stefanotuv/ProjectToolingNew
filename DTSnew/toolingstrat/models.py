from django.db import models

# Create your models here.
class AppType(models.Model):
    app_type = models.CharField(max_length=264,unique=True)
    def __str__(self):
        return self.app_type


class Region(models.Model):

    region_ID = models.CharField(max_length=3,unique=True)
    region_name = models.CharField(max_length=264,unique=True)

    def __str__(self):
        return self.region_ID

    def name(self):
        return self.region_name

class Application(models.Model):
    app_type = models.ForeignKey('AppType',on_delete=models.CASCADE)
    app_ID = models.CharField(max_length=6,unique=True)
    app_name = models.CharField(max_length=264,unique=True)

    def __str__(self):
        return self.app_ID

    def name(self):
        return self.app_name
