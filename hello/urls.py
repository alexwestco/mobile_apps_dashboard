from django.urls import path
from . import views
urlpatterns = [
    path('api/app_download/', views.AppDownloadListCreate.as_view() ),
]