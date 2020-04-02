from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='carlist'),
    path('<int:carlist_id>', views.singlecar, name="singlecar")
]
