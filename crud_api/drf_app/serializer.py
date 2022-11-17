from rest_framework import serializers

from drf_app.models import Student

def character_less_than_10(value):
    print(value, "validatorss")
    return value

class StudentModelSerailzier(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100, validators=[
                                 character_less_than_10])
    roll = serializers.CharField(max_length=100, validators=[
                                 character_less_than_10])

    def validate_name(self, value):
        print("validate name")
        
        return value

    def validate_roll(self, value):
        print("validate roll")
        
        return value


    def validate(self, data):
        print(data, "validate")
        return data
    class Meta:
        model = Student
        fields = "__all__"







# class StudentSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     name = serializers.CharField(max_length=100)
#     roll = serializers.CharField(max_length=100)

#     class Meta:
#         fields = ("id", "name", "roll")


#     def create(self, validated_data):
#         instance = Student.objects.create(**validated_data)
#         return instance

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get("name")
#         instance.roll = validated_data.get("roll")
#         instance.save()
#         return instance
