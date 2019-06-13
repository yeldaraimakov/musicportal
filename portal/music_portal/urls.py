from django.urls import path
from django.views.generic import TemplateView

from portal.music_portal import views
from portal.music_portal.views import VideosList

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('download/<int:music_id>/', views.download, name='download'),
    path('videos/', VideosList.as_view(), name='videos'),
    path('contacts/', TemplateView.as_view(template_name='music_portal/contacts.html'), name='contacts'),
]