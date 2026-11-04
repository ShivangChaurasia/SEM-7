from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=200)
    duration = models.IntegerField()


    def __str__(self):
        return self.name

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    is_active = models.BooleanField(default=True)

    # Add a foreign key to student
    student = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.name
