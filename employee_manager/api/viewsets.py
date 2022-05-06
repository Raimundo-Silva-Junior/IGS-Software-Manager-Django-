from rest_framework import viewsets
from employee_manager.api import serializers
from employee_manager import models

class MainViewset(viewsets.ModelViewSet):
    serializer_class = serializers.MainSerializers
    queryset = models.Employee.objects.all()

