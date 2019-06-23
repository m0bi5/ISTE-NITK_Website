from django.urls import path,include
from recruitments import views

urlpatterns = [
    path('', views.recruitments, name='recruitments'),
    path('progress/<applicant_id>/', views.application_progress, name='application_progress'),
    path('interview/',views.interview,name='interview'),
] 
