from django.db import models

# Create your models here.

class Category(models.Model) :
    name = models.CharField(max_length=128)

    def __str__(self) :
        return self.name

class State(models.Model) :
    name=models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Region(models.Model) :
    name=models.CharField(max_length=128)
    def __str__(self):
        return self.name

class Iso(models.Model) :
    name=models.CharField(max_length=128)
    def __str__(self):
        return self.name


class Site(models.Model):
    area_hectares = models.FloatField(null=True)
    longitude     = models.FloatField(null=True)
    latitude      = models.FloatField(null=True)
    justification = models.TextField(null=True)
    description   = models.TextField(null=True)
    name = models.CharField(max_length=128)
    year = models.IntegerField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    state=models.ForeignKey(State, on_delete=models.SET_NULL,null=True)
    iso=models.ForeignKey(Iso, on_delete=models.SET_NULL,null=True)
    region=models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)

    def __str__(self) :
        return self.name
