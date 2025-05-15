from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_employee, name='register'),
    path('register/<int:pk>/', views.register_employee, name='register_with_pk'),
    path('employees/', views.employee_list, name='employee_list'),  # 추가
    path('employees/delete/<int:pk>/', views.delete_employee, name='delete_employee'),  # 추가
    path('employee/delete-photo/<int:pk>/', views.delete_photo, name='delete_photo'),
    path('employee_list/export/', views.export_employees_excel, name='export_employees_excel'),
    path('departments/', views.department_list, name='department_list'),
    path('departments/delete/<int:pk>/', views.delete_department, name='delete_department'),  # ✅ 추가
    path('departments/edit/<int:pk>/', views.edit_department, name='edit_department'),  # ✅ 수정 URL
    path('ranks/', views.rank_list, name='rank_list'),
    path('ranks/edit/<int:pk>/', views.edit_rank, name='edit_rank'),
    path('ranks/delete/<int:pk>/', views.delete_rank, name='delete_rank'),
    path('positions/', views.position_list, name='position_list'),
    path('positions/edit/<int:pk>/', views.edit_position, name='edit_position'),
    path('positions/delete/<int:pk>/', views.delete_position, name='delete_position'),
    path('position-master/', views.position_master_list, name='position_master_list'),
    path('position-master/edit/<int:pk>/', views.edit_position_master, name='edit_position_master'),
    path('position-master/delete/<int:pk>/', views.delete_position_master, name='delete_position_master'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

