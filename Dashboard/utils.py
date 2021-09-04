from django.core.mail import EmailMessage

def emailNotification(title, body, receiver):
    
    email = EmailMessage(title,
    body,
    ["certificaciones.larroca@gmail.com"],
    reply_to=[receiver])
    try:
        email.send()
        return "mail succefully sended"
    except:
        return "error sending mail"