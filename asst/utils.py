import threading
from django.core import mail

class EmailThread(threading.Thread):
    def __init__(self, subject, plain_message, from_email, to_email, html_message):
        self.subject = subject
        self.plain_message = plain_message
        self.from_email = from_email
        self.to_email = to_email
        self.html_message = html_message
        super(EmailThread, self).__init__()

    def run(self):
        mail_send = mail.send_mail(self.subject, self.plain_message, self.from_email, [self.to_email], html_message=self.html_message)
        print('mail send successfully ', mail_send)