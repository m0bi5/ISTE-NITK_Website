from django.urls import path,include
from . import views

urlpatterns=[
    path('',views.view_meets, name='meets'),
    path('add/',views.add_meet,name='add_meet'),
]
