from django.urls import path
from .views import Midterm_A

urlpatterns = [
    path('midterma/', Midterm_A, name='midterma'),
]
