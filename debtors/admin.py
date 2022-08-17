from django.contrib import admin
from .models import Student, School

# Register your models here.

admin.site.register(Student)
admin.site.register(School)

admin.site.site_header = "Diftrak Debtor's School Dashboard"