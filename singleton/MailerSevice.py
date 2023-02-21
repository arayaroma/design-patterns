import smtplib, os, ssl

class MailerService:
    __instance = None

    @staticmethod
    def get_instance():
        if MailerService.__instance is None:
            MailerService()
        return MailerService.__instance

    def __init__(self):
            # Set up SMTP server configuration
            self.smtp_server = 'smtp.gmail.com'
            self.smtp_port = 465
            self.context = ssl.create_default_context()

            # Load email credentials from environment variables
            self.username = os.environ.get('EMAIL_USERNAME')
            self.password = os.environ.get('EMAIL_PASSWORD')
            self.sender_email = os.environ.get('EMAIL_SENDER')

            MailerService.__instance = self


    def send_email(self, recipient, subject, body):
        message = f'Subject: {subject}\n\n{body}'
        with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port, context=self.context) as server:
            server.login(self.username, self.password)
            server.sendmail(self.sender_email, recipient, message)