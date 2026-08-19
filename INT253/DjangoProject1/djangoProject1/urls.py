
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('about/', views.about),
    path('contact/', views.contact),
    path('services/', views.services),
    path('result/', views.result),
    path('weather/', views.weather),
    path('greetings/', views.greetings),
    path('items/', views.items),

]

#     *
#    ***
#   *****
#  *******
# *********