from email.message import EmailMessage
import ssl
import smtplib
class Email:

    def send_email(self, data):
        email_sender = 'nullmorales706@gmail.com'
        email_password = 'oochhjwfneezhpma'
        email_receiver = 'adrianmorales2635@gmail.com'
        body = data['body'] + " Sent By: " + data['sender']

        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['subject'] = data['subject']
        em.set_content(body)
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context= context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())