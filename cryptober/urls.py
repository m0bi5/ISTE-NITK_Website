from django.urls import path,include
from . import views

urlpatterns=[
    path('',views.instructions, name='instructions'),
    path('<team>/questions/<id>',views.questions,name='question_'+str(id)),
]
