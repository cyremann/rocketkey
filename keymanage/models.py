from django.db import models

#Sample Keys: AA5-2 FE12-18

class Employee(models.Model):
    def __str__(self):
        return self.first_name + " " + self.last_name
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

class Keycode(models.Model):
    def __str__(self):
        return self.name + self.number
    name = models.CharField(max_length=5) #AA or FE
    number = models.IntegerField() #5 or 12
    master = models.ForeignKey("self")

class Key(models.Model):
    def __str__(self):
        return self.code + "-" + self.number
    code = models.ForeignKey(Keycode) #AA5 or FE12
    number = models.IntegerField() #2 or 18
    assignee = models.ForeignKey(Employee) #self evident