# serializers.py

from rest_framework import serializers
from reyes_ivan_FINAL_app import models


class MiFormularioSerializer(serializers.Serializer):
    campo1 = serializers.CharField()
    campo2 = serializers.CharField()

    
class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Estudiante
        fields = '__all__'