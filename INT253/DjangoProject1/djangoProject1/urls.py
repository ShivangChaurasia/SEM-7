
from django.urls import path
from myapp import views


urlpatterns = [
    # path('', home),
    # path('about/', views.about),
    # path('contact/', views.contact),
    # path('services/', views.services),
    # path('result/', views.result),
    # path('weather/', views.weather),
    # path('greetings/', views.greetings),
    # path('items/', views.items),
    # path('Dgreetings/<str:name>/<int:time>/', views.Dgreetings),

    # path('home/<str:name>/<str:city>/', home),
    # path('menu/', views.menu_view, name='menu'),
    # path('result/', views.result, name='result'),

    path('home/',views.home),
    path('form/', views.simple_form),
]

