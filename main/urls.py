from django.urls import path 
from main import views

urlpatterns = [
    path('',views.index),
    path('delete/<int:id>/',views.delete,name="delete"),
    path('update/<int:id>/',views.update,name='update')
]
