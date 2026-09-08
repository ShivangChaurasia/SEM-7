from django.urls import path
from django.urls import re_path
# from . import views

from myapp import views

urlpatterns = [
    # path('', views.home),
    # path('about/', views.about),
    # path('contact/', views.contact),
    # path('student/<int:id>/<str:name>', views.student),
    # path('student_info/', views.student_info),

    path('method/', views.method_check),


    # path('student/<int:id>/', views.student),

    # re_path(r'^student/(?P<roll>\d{4})/$',views.student_regex),

    path('product/', views.product),
    re_path(r'^product/(?P<pdt_id>[A-Z]{3}\d{3})/$',views.pdt_regex),

    path('employee/', views.employee),
    re_path(r'^employee/(?P<emp_id>[A-Z]{3}\d{4})/$',views.emp_regex),


    path('validate/',views.validate_emp),
    re_path(r'^validate/(?P<id>EMP\d{4})/$',views.validate_regex),


    path('student/', views.student),
    path('student/profile/<int:id>/<str:name>',views.stu_profile),
    path('student/search/',views.stu_search),
    path('student/register/',views.stu_register),

]
