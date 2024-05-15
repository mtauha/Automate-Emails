import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

load_dotenv('pyvenv.env')

class EmailClient:
    def __init__(self):
        self.email = os.getenv('EMAIL')
        self.password = os.getenv('PASSWD')
        self.smtp_server = os.getenv('SMTP_SERVER')
        self.smtp_port = int(os.getenv('SMTP_PORT'))
        self.server = None

    def connect(self) -> bool:
        try:
            self.server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            self.server.starttls()
            return True
        except Exception as e:
            print(f"Connection failed: {str(e)}")
            return False
        
    def login(self) -> bool:
        try:
            self.server.login(self.email, self.password)
            return True
        except Exception as e:
            print(f"Login failed: {str(e)}")
            exit()
            return False

    def close(self) -> bool:
        if self.server:
            try:
                self.server.quit()
                exit()
            except Exception as e:
                print(f"Error closing connection: {str(e)}")
                return False
        else:
            print("No server connection exists.")
            return False
    
    def send(self, subject: str, body: str, to_email: str) -> bool:
        if not self.server:
            print("Server connection not established.")
            exit()

        message = MIMEMultipart()
        message['From'] = self.email
        message['To'] = to_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        try:
            print("Sending mail...")
            self.server.sendmail(self.email, to_email, message.as_string())
            print("Mail sent successfully.")
            return True
        except Exception as e:
            print(f"Error sending email: {str(e)}")
            exit()
