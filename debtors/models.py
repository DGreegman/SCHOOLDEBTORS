from django.db import models

# Create your models here.

class School(models.Model):
  school_name = models.CharField(max_length=100, null=True)
  school_admin = models.CharField(max_length=100, null=True)
  school_email = models.EmailField(null=True)
  school_address = models.CharField(max_length=100, null=True)
  school_location = models.CharField(max_length=100, null=True)
  school_phone_no = models.BigIntegerField(null=True)

class School(models.Model):
    first_name = models.CharField(max_length=150, null=True)
    last_name = models.CharField(max_length=150, null=True)
    parent_name = models.CharField(max_length=200, null=True)
    parent_email = models.EmailField(max_length=100, null=True)
    parent_phone_no = models.BigIntegerField(null=True)
    address = models.CharField(max_length=200, null=True)
    location = models.CharField(max_length=100, default="Lagos", null=True)
    admission_no = models.CharField(max_length=12, unique=True, null=True)
    fees_owed = models.IntegerField(null=True)
    last_school = models.ForeignKey(School, on_delete=models.CASCADE, null=True)