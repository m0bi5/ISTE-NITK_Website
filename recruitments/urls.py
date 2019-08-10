from django.urls import path,include
from recruitments import views

urlpatterns = [
    path('get_recruited/<rollno>', views.applicant_details, name='recruitments'),
    path('get_recruited/', views.applicant_details, name='recruitments'),
    path('progress/<applicant_rollno>/', views.application_progress, name='application_progress'),
    path('interview/',views.interview,name='interview'),
    path('interview/<sig>',views.sig_interview,name='sig_interview'),
    path('interview/<sig>/<rollno>',views.personal_interview,name='personal_interview'),
    path('questions/<applicant_rollno>/<sigs>',views.questions,name='questions'),
    path('edit_applicant/<sig>/<rollno>',views.edit_applicant,name='edit_applicant'),
]
