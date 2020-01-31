from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
admin.site.site_header='ISTE Website Admin Page'
admin.site.index_title='Admin page'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('events/',include('events.urls')),
    path('recruitments/',include('recruitments.urls')),
    path('projects/',include('projects.urls')),
    path('blogs/',include('blogs.urls')),
    path('account/',include('account.urls')),
    path('ckeditor/',include('ckeditor_uploader.urls')),
    path('cryptober/',include('cryptober.urls')),
    path('meets/',include('meet.urls')),
    path('obscura/',include('obscura.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
