# third party imports
import os
import sys
import logging

# django imports
import django_filters

# project level imports

# app level imports
from meals.models import Meal, Recipe


class MealFilter(django_filters.FilterSet):
    """
    Custom filter for Meal ViewSet
    """
    with_recipe = django_filters.Filter(method='filter_for_recipes')

    def filter_for_recipes(self, queryset, name, value):
        """
        Finds Meals which contain all the Recipe ID together
        :param queryset: queryset output from `get_queryset`
        :param value: query param
        :return: Meal queryset
        """
        try:
            recipes_ids_list = list(map(int, value.split(',')))
        except ValueError:
            return queryset

        recipes = Recipe.objects.filter(id__in=recipes_ids_list)

        for recipe in recipes:
            queryset = queryset.filter(recipes=recipe)

        return queryset

    class Meta:
        model = Meal
        fields = ['id', 'name', 'slug', 'with_recipe']
