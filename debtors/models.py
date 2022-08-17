from django.db import models

# Create your models here.

GENDER = (  ('Male','Male'), 
            ('Female','Female'),
    )

class School(models.Model):
    school_name = models.CharField(max_length=100)
    school_admin_name = models.CharField(max_length=100)
    school_email = models.EmailField(null=True)
    school_address = models.CharField(max_length=100, unique=True)
    school_location = models.CharField(max_length=100)
    school_phone_no = models.BigIntegerField()

class Student(models.Model):
    st_first_name = models.CharField(max_length=150)
    st_last_name = models.CharField(max_length=150)
    gender = models.CharField(max_length=15, choices=GENDER)
    parent_name = models.CharField(max_length=200)
    parent_email = models.EmailField(max_length=100)
    parent_phone_no = models.BigIntegerField()
    address = models.CharField(max_length=200)
    location = models.CharField(max_length=100, default="Lagos")
    admission_no = models.CharField(max_length=12, unique=True)
    fees_owed = models.IntegerField(null=True)
    last_school = models.ForeignKey(School, on_delete=models.CASCADE)


