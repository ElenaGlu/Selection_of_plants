from django.contrib import admin
from django.urls import path

from finder import views

urlpatterns = [
    path('', views.displays_plants_by_filters, name='displays_plants_by_filters'),
    path('<int:pk>/', views.displays_description_of_specific_plant, name='displays_description_of_specific_plant'),
    path('admin/', admin.site.urls),
]
