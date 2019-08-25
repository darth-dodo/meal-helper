# third party imports
import os
import sys
import logging

# django imports
import django_filters

# project level imports

# app level imports
from meals.models import Meal, Food


class MealFilter(django_filters.FilterSet):
    """
    Custom filter for Meal ViewSet
    """
    with_food = django_filters.Filter(method='filter_for_foods')

    def filter_for_foods(self, queryset, name, value):
        """
        Finds Meals which contain all the Foods ID together
        :param queryset: queryset output from `get_queryset`
        :param value: query param
        :return: Meal queryset
        """
        try:
            food_ids_list = list(map(int, value.split(',')))
        except ValueError:
            return queryset

        foods = Food.objects.filter(id__in=food_ids_list)

        for food in foods:
            queryset = queryset.filter(foods=food)

        return queryset

    class Meta:
        model = Meal
        fields = ['id', 'name', 'slug', 'with_food']
