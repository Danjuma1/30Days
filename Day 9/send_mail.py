import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


"""
Other way of doing this is using environment variables
"""

username = 'codefortunate@gmail.com'
password = 'SpecialAccount'


def send_mail(text="Email Body", subject="Hello World", from_email='Fortunate Coder <codefortunate@gmail.com', to_emails=None, html=None):
    assert isinstance(to_emails, list)
    msg = MIMEMultipart('alternative')
    msg["from"] = from_email
    msg["to"] = ", ".join(to_emails)
    msg["subject"] = subject

    txt_part = MIMEText(text, 'plain')
    msg.attach(txt_part)
    if html != None:
        html_part = MIMEText(html, 'html')
        msg.attach(txt_part)
    msg_str = msg.as_string()

    # Login to SMTP server
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(from_email, to_emails, msg_str)

    server.quit()
    # with smtplib.SMTP() as server:
    #     server.login()
    #     pass