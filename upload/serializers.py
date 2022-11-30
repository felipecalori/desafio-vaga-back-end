from rest_framework import serializers
from .models import Upload
from utils.cnba_converter import converter_CNAB, read_converted_file, remove_files
from interpreters.serializers import InterpreterSerializer

class UploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upload
        fields = '__all__'

    def create(self, validated_data):
        file = validated_data.get('file')
        if file.name != 'CNAB.txt':
            raise NameError("File name should be CNAB.txt")

        file_data = Upload.objects.create(**validated_data)
        converter_CNAB()

        json_info = read_converted_file()
        for info in json_info:
            serializer = InterpreterSerializer(data=info)
            serializer.is_valid(raise_exception=True)
            serializer.save()

        remove_files()
        return file_data