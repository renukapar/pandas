from rest_framework import serializers
from .models import PythonModel

class PythonSer(serializers.ModelSerializer):
    class Meta:
        model=PythonModel
        fields="__all__"