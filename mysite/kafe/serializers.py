from rest_framework import serializers
from .models import *
from django.utils.translation import override as translation_override
from django.utils.translation import get_language




class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class FoodSerializer(serializers.ModelSerializer):


    class Meta:
        model = Food
        fields = '__all__'

    def to_representation(self, instance):
        current_language  = get_language()
        translated_fields = [f"{field}_{current_language}" for field in ['name', 'description',]]

        data = super().to_representation(instance)
        translated_data = {field: data[field] for field in translated_fields if field in data}
        return translated_data



class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'



class FoodPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodPhoto
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'




