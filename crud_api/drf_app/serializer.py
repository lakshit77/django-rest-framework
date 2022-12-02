from rest_framework import serializers

from drf_app.models import Student

def character_less_than_10(value):
    # validators function
    print(value, "validatorss")
    return value

class StudentModelSerailzier(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100, validators=[character_less_than_10], help_text = "This is name field")
    roll = serializers.CharField(max_length=100, validators=[character_less_than_10])

    class Meta:
        model = Student
        fields = "__all__"

    def validate_name(self, value): 
        #Field Level Validation for name
        print("validate name")
        return value

    def validate_roll(self, value):
        #Field Level Validation for roll
        print("validate roll")
        return value

    def validate(self, data):
        #Object Level Validation for all fields
        print(data, "validate")
        return data


    def to_internal_value(self, data):
        print("inside to internal value", data)
        return super().to_internal_value(data)

    def to_representation(self,instance):
        obj = super(StudentModelSerailzier, self).to_representation(instance)
        print("inside to representation", obj)
        return obj


class DeleteSerialzier(serializers.Serializer):
    id = serializers.IntegerField()
class DeleteResponseSerialzier(serializers.Serializer):
    msg = serializers.CharField(help_text = "your data has beeen deletedddddd....")












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
