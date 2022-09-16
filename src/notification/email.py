import smtplib, requests, json
from email.message import EmailMessage

class notification:
    def __init__(self, registration_number):
        self.registration_number = registration_number
        
        # Collect default email settings via API
        url = "http://localhost:8000/api/v1/email/"
        headers = {
            'Content-Type': 'application/json'
        }
        payload = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        self.email_settings = json.loads(response.text)

    def email(self, email):
        # Collect Subject and Body Text
        # Format the Subject to ASCII charaters
        subject = self.email_settings[0]['smtp_subject']
        body = self.email_settings[0]['smtp_body']
        s1 = subject.format(self.registration_number)
        body = body.format(self.registration_number)
        #subject = s1.encode('ascii', 'ignore')
        
        # Create the email header
        msg = EmailMessage()
        msg.set_content(body)
        msg['From'] = self.email_settings[0]['smtp_user']
        msg['To'] = email
        msg['Subject'] = str(s1)
        
        try:
            smtp_server = smtplib.SMTP(self.email_settings[0]['smtp_server'], self.email_settings[0]['smtp_port'])
            smtp_server.starttls()
            smtp_server.login(self.email_settings[0]['smtp_user'], self.email_settings[0]['smtp_password'])
            smtp_server.sendmail(self.email_settings[0]['smtp_user'], email, str(msg))
            smtp_server.quit()
            print ("Email sent successfully!")
        except Exception as e:
            print("Somthing went wrong...", e)