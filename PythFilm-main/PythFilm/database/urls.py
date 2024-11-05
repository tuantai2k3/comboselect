# database/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('comboselect/', views.select_combo, name='select_combo'),
]