from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    gender_choices = [('M', 'Male'), ('F', 'Female')]

    user = models.OneToOneField(User, default=None, null=True, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=200, null=True)
    father_name = models.CharField(max_length=200, null=True)
    enrollment_no = models.CharField(max_length=200, null=True, unique=True)
    course = models.ForeignKey('Course', null=True, default=None, on_delete=models.CASCADE)
    dob = models.DateField(max_length=10, help_text='format: YYYY-MM-DD', null=True)
    gender = models.CharField(choices=gender_choices, max_length=1, default=None, null=True)
    room = models.OneToOneField('Room', blank=True, on_delete=models.CASCADE, null=True)
    room_allotted = models.BooleanField(default=True)

    def __str__(self):
        return self.student_name

class Room(models.Model):
    room_choice = [
        ('S', 'Single Occupancy'),
        ('D', 'Double Occupancy'),
        ('P', 'Reserved for Research Scholars'),
        ('B', 'Both Single and Double Occupancy')]
    
    no = models.CharField(max_length=5)
    name = models.CharField(max_length=10)
    room_type = models.CharField(choices=room_choice, max_length=1, default=None)
    vacant = models.BooleanField(default=False)
    hostel = models.ForeignKey('Hostel', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Hostel(models.Model):
    gender_choices = [('M', 'Male'), ('F', 'Female')]

    name = models.CharField(max_length=5)
    gender = models.CharField(choices=gender_choices, max_length=1, default=None, null=True)
    course = models.ManyToManyField('Course', default=None, blank=True)
    warden = models.CharField(max_length=100, blank=True)
    caretaker = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    room_choice = [
        ('S', 'Single Occupancy'),
        ('D', 'Double Occupancy'),
        ('P', 'Reserved for Research Scholars'),
        ('B', 'Both Single and Double Occupancy')]
    
    code = models.CharField(max_length=100, default=True)
    room_type = models.CharField(choices=room_choice, max_length=1, default='D')

    def __str__(self):
        return self.code 
