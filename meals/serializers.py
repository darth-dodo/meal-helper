# third party imports
import os
import sys
import logging


# django imports
from rest_framework import serializers


# project level imports
from utils.serializers_utils import EagerLoadingSerializerMixin
from utils.models import Tag

# app level imports
from meals.models import MealType, Meal, Food, MealPlan, NutritionalInformation


logger = logging.getLogger(__name__)


class MealTypeSerializer(serializers.ModelSerializer):
    """
    Model Serializer for MealType
    """
    class Meta:
        model = MealType
        fields = '__all__'


class MealTypeMiniSerializer(serializers.ModelSerializer):
    """
    Mini Model Serializer for MealType
    """
    class Meta:
        model = MealType
        fields = ('id', 'name', 'slug',)


class FoodSerializer(serializers.ModelSerializer, EagerLoadingSerializerMixin):
    """
    Model Serializer for Food
    """

    tags = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(), many=True)

    _PREFETCH_RELATED_FIELDS = ['tags']

    class Meta:
        model = Food
        fields = '__all__'


class FoodMiniSerializer(serializers.ModelSerializer):
    """
    Mini Model Serializer for Food
    """

    class Meta:
        model = Food
        fields = ('id', 'name', 'slug',)


class MealSerializer(serializers.ModelSerializer, EagerLoadingSerializerMixin):
    """
    Eager Loaded Model Serializer for Meal
    """

    meal_type = serializers.PrimaryKeyRelatedField(queryset=MealType.objects.all())
    foods = serializers.PrimaryKeyRelatedField(queryset=Food.objects.all(), many=True)
    tags = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(), many=True)

    foods_data = serializers.SerializerMethodField()
    meal_type_data = serializers.SerializerMethodField()

    _SELECT_RELATED_FIELDS = ['meal_type']
    _PREFETCH_RELATED_FIELDS = ['foods', 'tags']

    class Meta:
        model = Meal
        fields = ('id', 'name', 'slug', 'description', 'is_active', 'created_at', 'modified_at', 'foods', 'tags',
                  'meal_type', 'foods_data', 'meal_type_data')

    def get_meal_type_data(self, obj):
        return MealTypeMiniSerializer(obj.meal_type).data

    def get_foods_data(self, obj):
        return FoodMiniSerializer(obj.foods.all(), many=True).data


class MealMiniSerializer(serializers.ModelSerializer):
    """
    Mini Model Serializer for Meal
    """

    class Meta:
        model = Meal
        fields = ('id', 'name', 'slug',)


class MealPlanSerializer(serializers.ModelSerializer, EagerLoadingSerializerMixin):
    """
    Model Serializer for MealPlan
    """
    meals = serializers.PrimaryKeyRelatedField(queryset=Meal.objects.all(), many=True)

    _PREFETCH_RELATED_FIELDS = ['meals']

    meals_data = serializers.SerializerMethodField()

    class Meta:
        model = MealPlan
        fields = ('id', 'name', 'slug', 'description', 'meals_data', 'is_active', 'created_at',
                  'modified_at', 'meals')

    def get_meals_data(self, obj):
        return MealMiniSerializer(obj.meals.all(), many=True).data
