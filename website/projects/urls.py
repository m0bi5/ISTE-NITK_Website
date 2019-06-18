from django.urls import path,include
from . import views

urlpatterns=[
    path('',views.projects, name='projects_list'),
    path('projects/<id>',views.show_project,name='show_project'),
]
