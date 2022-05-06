from rest_framework import serializers
from employee_manager import models

class MainSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Employee
        fields = "__all__"