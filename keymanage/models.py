from django.db import models
import datetime

#Sample Keys: AA5-2 FE12-18

class Employee(models.Model):
    def __str__(self):
        return str(self.first_name) + " " + str(self.last_name)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

class Keycode(models.Model):
    def __str__(self):
        return str(self.name) + str(self.number)
    name = models.CharField(max_length=5) #AA or FE
    number = models.IntegerField() #5 or 12
    master = models.ForeignKey("self", null=True, blank=True)

class Key(models.Model):
    def __str__(self):
        return str(self.code) + "-" + str(self.number)
    code = models.ForeignKey(Keycode) #AA5 or FE12
    number = models.IntegerField() #2 or 18
    assignee = models.ForeignKey(Employee) #self evident
    date_issued = models.DateField(("Date"), default=datetime.date.today)
    date_returned = models.DateField(null=True, blank=True)
