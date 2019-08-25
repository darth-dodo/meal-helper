from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_swagger.views import get_swagger_view
from rest_framework.documentation import include_docs_urls

from meal_planner.settings.base import get_env_variable


schema_view = get_swagger_view(title='Meal Planner Swagger API')

# project level imports
from meal_planner.settings.base import ADMIN_SITE_HEADER


admin.site.site_header = ADMIN_SITE_HEADER

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),  # grappelli URLS
    url(r'^', admin.site.urls),
    url(r'^auth/login/$', obtain_jwt_token),
    path(r'api-docs/', include_docs_urls(title='Meal Planner API')),
    url(r'^api/meals/', include('meals.urls')),
    path(r'swagger-docs/', schema_view),
]


if get_env_variable('DEBUG_TOOLBAR'):
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
