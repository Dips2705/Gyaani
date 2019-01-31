from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=10)
    sem = models.CharField(max_length=10)
    def __str__(self):
        return self.name

class Ftype(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    module = models.CharField(max_length=30)

    def __str__(self):
        return self.module

class Fupload(models.Model):
    name = models.CharField(max_length=100)
    file_type = models.CharField(max_length=10)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    ftype = models.ForeignKey(Ftype, on_delete=models.SET_NULL, null=True)
    up_file = models.FileField(default="background.jpg")

    def __str__(self):
        return self.name