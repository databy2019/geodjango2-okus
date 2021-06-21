"""django1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#from django.contrib.auth import views as auth_views
from djangoapp1 import views

admin.site.site_header = 'Aplikasi WebGIS Kabupaten OKU Selatan'
admin.site.site_title = 'Admin WebGIS Kabupaten OKU Selatan'
admin.site.index_title = 'WebGIS Admin'
admin.empty_value_display ='** -- **'

urlpatterns = [
    #path('', views.home, name='home'),
    path('', include('djangoapp1.urls')),
    path('signup/', views.signup, name='signup'),
    path('daftar/', views.daftar, name='daftar'),
    path('activate/<uidb64>/<token>/',views.activate, name='activate'),
    path('admin/', admin.site.urls),
    path('secret/', views.secret_page, name='secret'),
    path('secret2/', views.SecretPage.as_view(), name='secret2'),
    path('accounts/', include('django.contrib.auth.urls')),
    #path('contact/', views.contact, name='contact'),
    #path('accounts/', include('django.contrib.auth.urls')),
]
