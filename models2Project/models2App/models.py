from django.db import models

# Dog model
class Dog(models.Model):
    name = models.CharField(max_length=200)
    race = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)

# Account model
class Account(models.Model):
    username = models.CharField(max_length=200)
    realName = models.CharField(max_length=200)
    accountNumber = models.IntegerField()
    balance = models.IntegerField()