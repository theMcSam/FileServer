from django.urls import path
from .views import DownloadView, search_file, email_form, send_mail, preview_file

urlpatterns = [
    path('download/<int:id>/', DownloadView.as_view(), name='download'),
    path('search/', search_file,name='file_search'),
    path('email_form/<int:id>/', email_form,name='email_form'),
    path('send_mail/<int:id>', send_mail,name='send_mail'),
    path('preview/<int:id>', preview_file,name='preview_file'),
    path('search',search_file,name='file_search'),
]
