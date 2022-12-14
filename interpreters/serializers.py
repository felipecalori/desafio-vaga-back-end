from rest_framework import serializers
from .models import Interpreter
import decimal


class InterpreterSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Interpreter
        fields = '__all__'

    def create(self, validated_data):
        return Interpreter.objects.get_or_create(**validated_data)[0]
