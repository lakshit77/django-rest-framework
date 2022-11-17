from rest_framework import serializers

from drf_app.models import Student

class StudentModelSerailzier(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = "__all__"
        # fields = ("id", "name", "roll")

class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    roll = serializers.CharField(max_length=100)

    class Meta:
        fields = ("id", "name", "roll")


    def create(self, validated_data):
        instance = Student.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name")
        instance.roll = validated_data.get("roll")
        instance.save()
        return instance
