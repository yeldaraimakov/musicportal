from django.urls import path
from django.views.generic import TemplateView


from portal.music_portal import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('download/<int:music_id>/', views.download, name='download'),
    path('videos/', TemplateView.as_view(template_name='music_portal/videos.html'), name='videos'),
    path('contacts/', TemplateView.as_view(template_name='music_portal/contacts.html'), name='contacts'),
]