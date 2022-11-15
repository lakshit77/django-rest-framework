from rest_framework import serializers
from drf_app.models import Student


class TechsunamiStringField(serializers.CharField):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def run_validation(self, data):
        
        if not isinstance(data, str):
            raise serializers.ValidationError("Data enter should be string type")

        data = data.upper()

        return super().run_validation(data)


class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = TechsunamiStringField(max_length=100)
    roll = serializers.CharField(max_length=100)

    class Meta:
        model = Student
        fields = "__all__"
