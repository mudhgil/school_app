from django.db import models

class School(models.Model):
    school_name = models.CharField(max_length=100)
    state = models.CharField(max_length=50)

    def __str__(self):
        return self.school_name


class Teacher(models.Model):
    teacher_name = models.CharField(max_length=100)
    age = models.IntegerField()
    subject = models.CharField(max_length=50)
    school_name = models.ForeignKey(School, on_delete=models.CASCADE, related_name="teacher")

    def __str__(self):
        return self.teacher_name

class Student(models.Model):
    student_name = models.CharField(max_length=100)
    age = models.IntegerField()
    school_name = models.ForeignKey(School, on_delete=models.CASCADE, related_name="student")

    def __str__(self):
        return self.student_name
