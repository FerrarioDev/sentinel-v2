from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_assets/', views.add_asset, name="create"),
]
