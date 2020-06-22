
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from altapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('altapp.urls')),
    path('contact.html', views.contact, name='contact'),
]


urlpatterns += staticfiles_urlpatterns()
