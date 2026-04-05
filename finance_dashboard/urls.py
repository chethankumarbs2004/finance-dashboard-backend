from django.urls import path, include
from rest_framework.routers import DefaultRouter
from records.views import RecordViewSet
from dashboard.views import DashboardSummary, FrontendDashboard
from users.views import UserViewSet
from django.contrib import admin

router = DefaultRouter()
router.register(r'records', RecordViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', DashboardSummary.as_view(), name='dashboard'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/dashboard/', DashboardSummary.as_view(), name='dashboard_api'),
    path('frontend/', FrontendDashboard.as_view(), name='frontend_dashboard'),
]
