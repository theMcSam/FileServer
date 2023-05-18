from django.core.mail import EmailMessage
import mimetypes

def send_email(to, attachment, file_name, subject, body):
    from_email = "djangofileserver@gmail.com"
    email = EmailMessage(subject, body, from_email, [to])
    if attachment:
        mime,_ = mimetypes.guess_type(attachment)
    
        # Attach the file
        file_path = attachment
        with open(file_path, 'rb') as file:
            email.attach(filename=file_name.split("/")[1] , content=file.read(), mimetype=mime)
    file_obj.number_of_emails += 1
    file_obj.save()
    # Send the email
    if email.send():
        return 1
    
    return 0
    