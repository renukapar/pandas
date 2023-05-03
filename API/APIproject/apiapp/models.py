from django.db import models

# Create your models here.
class PythonModel(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=10)
    age=models.IntegerField()
    email=models.EmailField()
    mobile=models.BigIntegerField()