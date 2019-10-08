from django.contrib import admin

from meals.models import MealType, Meal, Recipe, NutritionalInformation, MealPlan, Ingredient

# Register your models here.
class MealAppAbstractAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'code', 'name', 'description', 'slug']
    search_fields = ['name', 'slug']
    list_display_links = ['__str__']
    readonly_fields = ('slug',)
    ordering = ['-created_at']

    class Meta:
        abstract = True


class MealTypeAdmin(MealAppAbstractAdmin):

    class Meta:
        model = MealType


admin.site.register(MealType, MealTypeAdmin)


class MealAdmin(MealAppAbstractAdmin):
    list_display = ['__str__', 'code', 'name', 'description', 'slug', 'meal_type']
    list_filter = ['meal_type']

    class Meta:
        model = Meal


admin.site.register(Meal, MealAdmin)


class RecipeAdmin(MealAppAbstractAdmin):

    class Meta:
        model = Recipe


admin.site.register(Recipe, RecipeAdmin)


class MealPlanAdmin(MealAppAbstractAdmin):

    class Meta:
        model = MealPlan


admin.site.register(MealPlan, MealPlanAdmin)


class IngredientAdmin(MealAppAbstractAdmin):

    class Meta:
        model = Ingredient


admin.site.register(Ingredient, IngredientAdmin)


admin.site.register(NutritionalInformation)
