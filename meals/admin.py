from django.contrib import admin
from jet.admin import CompactInline

from meals.models import MealType, Meal, Food, NutritionalInformation, MealPlan

# Register your models here.
# admin.site.register(MealType)
admin.site.register(Meal)
admin.site.register(Food)
admin.site.register(NutritionalInformation)
admin.site.register(MealPlan)


class MealTypesInline(CompactInline):
    model = MealType
    can_delete = False


class MealTypesAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'description', 'slug', 'name')
    search_fields = ['name', 'slug']
    list_display_links = ['__str__']
    readonly_fields = ('slug',)

    class Meta:
        model = MealType


admin.site.register(MealType, MealTypesAdmin)
