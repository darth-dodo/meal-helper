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
from meals.models import MealType, Meal, Recipe, MealPlan, NutritionalInformation


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


class RecipeSerializer(serializers.ModelSerializer, EagerLoadingSerializerMixin):
    """
    Model Serializer for Recipe
    """

    tags = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(), many=True)

    _PREFETCH_RELATED_FIELDS = ['tags']

    class Meta:
        model = Recipe
        fields = '__all__'


class RecipeMiniSerializer(serializers.ModelSerializer):
    """
    Mini Model Serializer for Recipe
    """

    class Meta:
        model = Recipe
        fields = ('id', 'name', 'slug',)


class MealSerializer(serializers.ModelSerializer, EagerLoadingSerializerMixin):
    """
    Eager Loaded Model Serializer for Meal
    """

    meal_type = serializers.PrimaryKeyRelatedField(queryset=MealType.objects.all())
    recipes = serializers.PrimaryKeyRelatedField(queryset=Recipe.objects.all(), many=True)
    tags = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(), many=True)

    recipes_data = serializers.SerializerMethodField()
    meal_type_data = serializers.SerializerMethodField()

    _SELECT_RELATED_FIELDS = ['meal_type']
    _PREFETCH_RELATED_FIELDS = ['recipes', 'tags']

    class Meta:
        model = Meal
        fields = ('id', 'name', 'slug', 'description', 'is_active', 'created_at', 'modified_at', 'recipes', 'tags',
                  'meal_type', 'recipes_data', 'meal_type_data')

    def get_meal_type_data(self, obj):
        return MealTypeMiniSerializer(obj.meal_type).data

    def get_recipes_data(self, obj):
        return RecipeMiniSerializer(obj.recipes.all(), many=True).data


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
