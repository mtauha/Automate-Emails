from EmailClient import EmailClient
import datetime


today = datetime.date.today()
instance = EmailClient()
instance.connect()
instance.login()

client_mails = ["denischristopher798@gmail.com"]
subject = "Testing Script"
report_body = f"""
Dear Clients,

Testing Email script at date {today}

"""
for mail in client_mails:
    instance.send(subject, report_body, mail)


instance.close()

del instance