from django.urls import path
from django.views.generic import TemplateView 
from rest_framework_simplejwt.views import TokenRefreshView
from .views import ResidentListCreateView, ResidentDetailView, UserListView, CustomTokenObtainPairView, LogoutView


urlpatterns = [
    #login , register, logout routing
    path('login/', TemplateView.as_view(template_name='login.html'), name='login'),
    path('register/', TemplateView.as_view(template_name = 'registration.html'), name='registration'),
    path("api/logout/", LogoutView.as_view(), name="logout"),
    
    #routing for viewing residents and specific resident
    path('residents/', ResidentListCreateView.as_view(), name='resident-list-create'),
    path('residents/<int:pk>/', ResidentDetailView.as_view(), name='resident-detail'),
    path('users/', UserListView.as_view(), name='user-list'),
    
    
    #token routing for login and refresh token
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    #dashboards admin, employee, and residents
    path('admin_dashboard/', TemplateView.as_view(template_name='admin/admin_dashboard.html'), name='admin_dashboard'),
    path('employee_dashboard/', TemplateView.as_view(template_name='employee/employee_dashboard.html'), name='employee_dashboard'),
    path('resident_dashboard/', TemplateView.as_view(template_name='residents/resident_dashboard.html'), name='resident_dashboard'),
]
