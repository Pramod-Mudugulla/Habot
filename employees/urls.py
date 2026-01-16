from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet
from .health import health_check

router = DefaultRouter()
router.register(r"employees", EmployeeViewSet, basename="employees")

urlpatterns = [
    path("health/", health_check, name="health"),
] + router.urls
