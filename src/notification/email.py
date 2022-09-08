from importlib import import_module
import smtplib 
from email.message import EmailMessage
from .models import EmailSettings


class notification:
    def __init__(self, registration_number):
        self.registration_number = registration_number

    def email(self, email):
        # Collect default email settings
        email_settings = EmailSettings.objects.get(pk=1)
        smtp_server_address = email_settings.smtp_server
        smtp_port = email_settings.smtp_port
        smtp_user = email_settings.smtp_user
        smtp_password = email_settings.smtp_password
        smtp_protocol = email_settings.smtp_protocol

        # Collect Subject and Body Text
        # Format the Subject to ASCII charaters
        s1 = email_settings.smtp_subject.format(self.registration_number)
        body = email_settings.smtp_body.format(self.registration_number)
        #subject = s1.encode('ascii', 'ignore')
        
        # Create the email header
        msg = EmailMessage()
        msg.set_content(body)
        msg['From'] = smtp_user
        msg['To'] = email
        msg['Subject'] = str(s1)
        
        try:
            smtp_server = smtplib.SMTP(smtp_server_address, smtp_port)
            smtp_server.starttls()
            smtp_server.login(smtp_user, smtp_password)
            smtp_server.sendmail(smtp_user, email, str(msg))
            smtp_server.quit()
            print ("Email sent successfully!")
        except Exception as e:
            print("Somthing went wrong...", e)