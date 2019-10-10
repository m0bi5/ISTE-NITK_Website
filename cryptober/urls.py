from django.urls import path,include
from . import views

urlpatterns=[
    path('instructions',views.instructions, name='instructions'),
    path('<team>/questions/<id>',views.questions,name='question_'+str(id)),
]
