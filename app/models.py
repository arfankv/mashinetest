from django.db import models

CHOICES = (
    ('python', 'python'),
    ('flutter', 'Flutter'),
    ('php', 'php'),
    ('Mernstack', 'MERNSTACK'),
    ('.net', '.Net'),
)
# Create your models here.
class Student(models.Model):

    Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Number = models.CharField(max_length=10)
    age = models.CharField(max_length=10)
    course = models.CharField(max_length=10, choices=CHOICES, default='python')


class Cource(models.Model):
    course = models.CharField(max_length=100)
    Name = models.CharField(max_length=10)