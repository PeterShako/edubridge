from django.urls import path
from .views import upload_files, download_file

urlpatterns = [
    path('', upload_files, name='upload_files'),
    path('download/<int:file_id>/', download_file, name='download_file'),
]
