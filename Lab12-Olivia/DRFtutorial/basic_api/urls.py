from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from basic_api import views


urlpatterns = [
    path('basic/', views.API_objects.as_view()),    
    path('basic/<int:pk>/', views.API_objects_detail.as_view()),
    path('mahasiswa/', views.MahasiswaList.as_view(), name='mahasiswa-list'),
    path('mahasiswa/<int:pk>/', views.MahasiswaDetail.as_view(), name='mahasiswa-detail'),
    path('dosen/', views.DosenList.as_view(), name='dosen-list'),
    path('dosen/<int:pk>/', views.DosenDetail.as_view(), name='dosen-detail'),
    path('dashboard/', views.dashboard_list, name='dashboard'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/tambah/', views.post_create, name='post_create'),
]   

urlpatterns = format_suffix_patterns(urlpatterns)
#kenapa digituin karena kalo misal mau bikin objek 