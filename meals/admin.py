from django.contrib import admin

from meals.models import MealType, Meal, Food, NutritionalInformation, MealPlan

# Register your models here.
admin.site.register(MealType)
admin.site.register(Meal)
admin.site.register(Food)
admin.site.register(NutritionalInformation)
admin.site.register(MealPlan)

