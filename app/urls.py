from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('map/', views.show_map, name='show_map'),
    path('login/', views.login_view, name='login'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('student_login/', views.student_login, name='student_login'),
    path('guest_dashboard/', views.guest_dashboard, name='guest_dashboard'),
]