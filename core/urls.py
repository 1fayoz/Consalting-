
from django.contrib import admin
from django.urls import path
from app.views import home, about, project,blog,servis,contact
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home, name='home'),
    path('about.html/', about, name='about' ),
    path('project.html/', project, name='project'),
    path('services.html/', servis, name='servis'),
    path('blog.html/', blog, name='blog'),
    path('contact.html', contact, name='contact')


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, 
                          document_root=settings.STATIC_ROOT)