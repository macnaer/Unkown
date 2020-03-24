from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='carslist'),
    path('<int:carslist_id>', views.singlecar, name="carlist")
]
