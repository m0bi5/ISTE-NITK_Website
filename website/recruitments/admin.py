from django.contrib import admin
<<<<<<< HEAD
from .models import ApplicantPasscode
# Register your models here.
admin.site.register(ApplicantPasscode)
=======
from .models import *
# Register your models here.

admin.site.register(Applicant)
admin.site.register(ApplicantResponses)
admin.site.register(SIGRound)
admin.site.register(Question)
>>>>>>> fc5014123bf93ac65610d1fb1d52524d45f940e5
