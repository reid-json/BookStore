from django.core.mail import send_mail

def send_email_notification(to_email, subject, message):
    send_mail(
        subject,
        message,
        'shlvesbookstore@gmail.com',
        [to_email],
        fail_silently=False
    )