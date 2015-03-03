from django.db import models
from django.forms import ModelForm
from django import forms

WEEKS2 = 2
WEEKS8 = 8
DURATION_CHOICES = ((WEEKS2, '2 Weeks'),
                    (WEEKS8, '8 Weeks'))

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(help_text="Provide some information about what students will learn.")
    instructor = models.CharField(max_length=200)
    duration = models.IntegerField(max_length=2, choices=DURATION_CHOICES, default=WEEKS2)
    course_art = models.FileField(upload_to='img',)

class CourseForm(ModelForm):
    duration = forms.ChoiceField(widget=forms.RadioSelect, choices=DURATION_CHOICES)
    class Meta:
        model = Course
        fields = ['title', 'description', 'instructor', 'duration', 'course_art']
