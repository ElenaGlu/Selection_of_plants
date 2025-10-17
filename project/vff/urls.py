from django.urls import path

from finder import views

urlpatterns = [
    path('', views.filter_plant, name='filter_plant'),
    path('<int:pk>/', views.display_content_plant, name='display_content_plant'),
]
