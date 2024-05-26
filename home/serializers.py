from  rest_framework import serializers
from .models import Person,UploadedImage

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'
    def validate_age(self, age):
        # Custom validation logic for the 'some_field' field
        if age < 18:
            raise serializers.ValidationError("age required greater then 18")
        return age
class UploadedImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedImage
        fields = ('id', 'image','file' ,'uploaded_at')