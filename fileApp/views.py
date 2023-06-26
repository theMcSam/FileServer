from django.shortcuts import render, redirect
from django.db.models import Q
from mailer import send_email
from django.http import FileResponse
from django.http import HttpResponse
from django.views import View
from django.shortcuts import get_object_or_404
from django.contrib import messages
from file_server.settings import BASE_DIR
from .models import File
from .forms import EmailAttachementForm

import os
import mimetypes

# Create your views here.
class DownloadView(View):
    def get(self, request, id):
        # Logic to generate the file
        file = get_object_or_404(File,pk=id)
        file_name = str(file.file.name).split("/")[1]

        file.number_of_downloads += 1
        file.save()

        file_path = os.path.join(BASE_DIR, str(file.file))

        # Open the file using FileResponse and serve it to the user
        with open(file_path, 'rb') as file:
            response = FileResponse(file)
            response = HttpResponse(file, content_type='')
            response['Content-Disposition'] = f'attachment; filename="{file_name}"'
            return response

def search_file(request):
    query = request.GET.get('search')
    
    if query:
        files = File.objects.filter(
            Q(file__icontains=query) | Q(description__icontains=query)
        )
    else:
        files = File.objects.none()
    
    return render(request, 'search.html', {'files': files})

def email_form(request, id):
    file = get_object_or_404(File, pk=id)
    file_name = str(file.file.name).split("/")[1]
    return render(request, "email_form.html", {"form": EmailAttachementForm(), "file": file, "file_name":file_name})

def send_mail(request, id):
    mail_to = request.POST["mail_to"]
    subject = request.POST["subject"]
    body = request.POST["body"]

    file = get_object_or_404(File, pk=id)
    file_path = os.path.join(BASE_DIR, str(file.file))
    file_name = str(file.file.name).split("/")[1]

    if send_email(to=mail_to, attachment=file_path, 
                  file_name=str(file.file.name),
                   subject=subject, body=body, file_obj=file):
        file.number_of_emails += 1
        file.save()
        return render(request, "attachment_sent.html", {"mailsent": True})
    
    return render(request, "attachment_sent.html", {"mailsent": False})

def preview_file(request, id):
    file = get_object_or_404(File,pk=id)
    file_path = os.path.join(BASE_DIR, str(file.file))
    mime_type, _ = mimetypes.guess_type(file_path)
    return FileResponse(open(file_path, 'rb'), content_type=mime_type)
