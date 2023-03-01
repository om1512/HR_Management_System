from . import views
from django.urls import path

urlpatterns = [
    path('', views.performance, name='performance'),
    path('payroll', views.payroll, name='payroll'),
    path('recruitment', views.recruitment, name='recruitment'),
    path('leave_notes', views.leaveNotes, name='leaveNotes'),
    path('add_employee', views.addEmployee, name='addEmployee'),
    path('logout', views.logout, name='logout'),
    path('addPerformance',views.addPerformance,name='addPerformance')
]
