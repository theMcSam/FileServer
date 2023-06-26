from django.core.mail import EmailMessage
import mimetypes

def send_email(**email_details):

    to = email_details["to"]
    body = email_details["body"]
    subject = email_details["subject"] 
    attachment = email_details["attachment"] if "attachment" in email_details else False
    file_name = email_details["file_name"] if "file_name" in email_details else "nothing"

    from_email = "djangofileserver@gmail.com"
    email = EmailMessage(subject, body, from_email, [to])
    
    if attachment:
        mime,_ = mimetypes.guess_type(attachment)
    
        # Attach the file
        file_path = attachment
        with open(file_path, 'rb') as file:
            email.attach(filename=file_name.split("/")[1] , content=file.read(), mimetype=mime)

    # Send the email
    if email.send():
        return True
    return False
    