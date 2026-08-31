
from django.urls import path
from myapp.views import home


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

    path('home/<str:name>/<str:city>/', home),
]

