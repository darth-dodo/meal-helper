from rest_framework.routers import DefaultRouter

from meals.views import MealTypeViewSet, MealViewSet, FoodViewSet, MealPlanViewSet

router = DefaultRouter()

router.register(r'^meal-type', MealTypeViewSet)
router.register(r'^meal', MealViewSet)
router.register(r'^food', FoodViewSet)
router.register(r'^meal-plan', MealPlanViewSet)

urlpatterns = router.urls
