from django.urls import path

from portal.music_portal import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('download/<int:music_id>/', views.download, name='download'),
]