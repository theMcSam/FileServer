from django.core.mail import EmailMessage
import mimetypes

def send_email(**email_details):
    try:
        to = email_details["to"]
        body = email_details["body"]
        subject = email_details["subject"] 
        attachment = email_details["attachment"] | False
        file_name = email_details["file_name"] | "nothing"

        from_email = "djangofileserver@gmail.com"
        email = EmailMessage(subject, body, from_email, [to])
        
        if attachment:
            mime,_ = mimetypes.guess_type(attachment)
        
            # Attach the file
            file_path = attachment
            with open(file_path, 'rb') as file:
                email.attach(filename=file_name.split("/")[1] , content=file.read(), mimetype=mime)

        # Send the email
        email.send()
        return 1

    except:
        return 0
        