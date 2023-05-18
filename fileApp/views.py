from django.shortcuts import render
from mailer import send_email
from django.http import FileResponse
from django.http import HttpResponse
from django.views import View
from django.shortcuts import get_object_or_404
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
    ...

def email_form(request, id):
    file = get_object_or_404(File, pk=id)
    file_name = str(file.file.name).split("/")[1]
    return render(request, "email_form.html", {"form": EmailAttachementForm(), "file": file, "file_name":file_name})
    ...

def send_mail(request, id):
    mail_to = request.POST["mail_to"]
    subject = request.POST["subject"]
    body = request.POST["body"]

    file = get_object_or_404(File, pk=id)
    file_path = os.path.join(BASE_DIR, str(file.file))

    if send_email(to=mail_to, attachment=file_path, 
                  file_name=str(file.file.name),
                   subject=subject, body=body, file_obj=file):
        file.number_of_emails += 1
        file.save()
        return HttpResponse("<h1>Mail Sent Successfully<h1>")
    
    return HttpResponse("<h1>Unable to send Mail<h1>")

def preview_file(request, id):
    file = get_object_or_404(File,pk=id)
    file_path = os.path.join(BASE_DIR, str(file.file))
    mime_type, _ = mimetypes.guess_type(file_path)
    return FileResponse(open(file_path, 'rb'), content_type=mime_type)
