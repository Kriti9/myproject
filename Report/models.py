from django.db import models

class Employee(models.Model):
    Name = models.CharField(max_length=80)
    Email = models.EmailField()
    PhoneNumber = models.IntegerField(default=0)
    Adhar=models.ImageField('Adhar_card')
    Pan =models.ImageField('Pan_card')
    PassBookFirstPage=models.ImageField('PassBookFirstPage')

    # Create your models here.
    def __str__(self):
        return self.Name
class Attendence(models.Model):
    Attendence=models.DateField()
    present=models.BooleanField(default=False)


    
