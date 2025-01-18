from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Note(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Ensure this field exists
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
# Custom User model
class CustomUser(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# Course model
class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


# Learner model with Many-to-Many relationship through an intermediate table
class Learner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Connect to Django's built-in User
    student_id = models.CharField(max_length=100, unique=True)
    full_name = models.CharField(max_length=255)
    enrolled_courses = models.ManyToManyField(Course, through='LearnerCourseEnrollment')
    date_of_birth = models.DateField()

    def __str__(self):
        return self.full_name


# manage the relationship between Learner and Course
class LearnerCourseEnrollment(models.Model):
    learner = models.ForeignKey(Learner, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_enrolled = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.learner} enrolled in {self.course} on {self.date_enrolled}"


# Image Upload model
class ImageUpload(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return f"Image by {self.user}"
