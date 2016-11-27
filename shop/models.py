from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255,unique=True)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.name


class Item(models.Model):
    code = models.IntegerField(unique=True)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category)
    description = models.TextField(max_length=500)
    image = models.URLField(max_length=100, default="https:\\")

    def __str__(self):
        return self.name







