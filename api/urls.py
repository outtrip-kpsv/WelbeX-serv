from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from table.views import TableSet

router = DefaultRouter()
router.register('table', TableSet, basename='table')

urlpatterns = [
    path("", include(router.urls)),
    path('admin/', admin.site.urls),
]
