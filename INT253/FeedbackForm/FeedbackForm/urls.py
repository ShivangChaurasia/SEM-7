from django.urls import path
from myapp.views import feedback_view

urlpatterns = [
    path('', feedback_view, name='home'),
    path('feedback/', feedback_view, name='feedback'),
]
