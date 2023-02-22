from django.shortcuts import get_object_or_404
from rest_framework import serializers
from django.db import transaction

from calories_tracker.models import FoodItem, UserFood
from users.models import User
from users.serializer import UserDetailsSerializer


class FoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields = (
            'id', 'food_name', 'calories', 'protein', 'fat'
        )

        def create(self, validated_data):
            with transaction.atomic():
                food_item_obj = FoodItem.objects.create(
                    food_name=validated_data('food_name'),
                    calories=validated_data('calories'),
                    protein=validated_data('protein'),
                    fat=validated_data('fat')
                )

            return food_item_obj

        def update(self, instance, validated_data):
            with transaction.atomic():
                instance.food_name = validated_data['food_name']
                instance.calories = validated_data['calories']
                instance.protein = validated_data['protein']
                instance.fat = validated_data['fat']
                instance.save()
            return instance


class UserFoodSerializer(serializers.ModelSerializer):
    food_id = serializers.IntegerField(required=False, write_only=True)
    food = FoodItemSerializer(read_only=True)
    user_id = serializers.IntegerField(required=False, write_only=True)
    user = UserDetailsSerializer(read_only=True)

    class Meta:
        model = UserFood
        fields = (
            'id', 'user', 'user_id', 'food', 'food_id'
        )

        def create(self, validated_data):
            with transaction.atomic():
                user_obj = get_object_or_404(User, id=validated_data.get('user'))
                food_item_obj = get_object_or_404(FoodItem, id=validated_data.get('food'))

                user_food_obj = UserFood.objects.create(
                    user=user_obj,
                    food=food_item_obj
                )

            return user_food_obj

        def update(self, instance, validated_data):
            with transaction.atomic():
                instance.food_name = validated_data['food_name']
                instance.calories = validated_data['calories']
                instance.protein = validated_data['protein']
                instance.fat = validated_data['fat']
                instance.save()
            return instance
