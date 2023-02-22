from MailerSevice import MailerService

def main():
    mailer = MailerService.get_instance()
    recipient = 'darayaroma@gmail.com'
    subject = 'Python Script'
    body = 'Sending a email from a python script using the singleton design pattern'

    mailer.send_email(recipient, subject, body)
    del mailer

if __name__ == '__main__':
    main()