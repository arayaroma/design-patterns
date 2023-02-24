from MailerSevice import MailerService

def main():
    mailer = MailerService.get_instance()
    recipient = 'klubarco@gmail.com'
    subject = 'Tremendisimo'
    body = 'tremendisimo script que le estoy mandando, que tal guapiss jijijiji, las espio en linux'

    mailer.send_email(recipient, subject, body)
    del mailer

if __name__ == '__main__':
    main()