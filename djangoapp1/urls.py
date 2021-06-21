from django.urls import path
from djangoapp1 import views

urlpatterns = [
    #path('/', views.todolist, name='todolist'),
    path('contact/', views.contact, name='contact'),
    path('', views.home, name='home'),
    path('kecamatan/', views.KecamatanData, name='kecamatan'),
    path('infrastruktur/', views.infrastruktur, name='infrastruktur'),
    path('sarpras/', views.SarprasData, name='sarpras'),
    path('infrastrukturjalan/', views.InfrastrukturJalanData, name='infrastrukturjalan'),
    path('jalanpropinsi/',views.JalanPropinsiData, name='jalanpropinsi'),
    path('jalankabupaten/',views.JalanKabupatenData, name='jalankabupaten'),
    path('dinas/',views.DinasData, name='dinas'),
]
