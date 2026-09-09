
from django.urls import path
from django.urls import re_path
from . import views

urlpatterns = [

    # Q3---Ans:
    path('search/',views.search),


    # Q4---Ans
    re_path(r'^employee/(?P<emp_id>E\d{3})/$',views.employee),
]
