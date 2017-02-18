import smtplib
from email.mime.text import MIMEText


class Email():
    def __init__(self, gmail_user, gmail_password):
        self.server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        self.server.ehlo()
        self.server.login(gmail_user, gmail_password)

    def sendmail(self, _from, _to, subject, content):
        if type(_to) == str:
            _to = [_to]
        msg = MIMEText(content, 'plain', 'utf-8')
        msg["Subject"] = subject
        msg["From"] = _from
        msg["To"] = ", ".join(_to)
        self.server.sendmail(_from, _to, msg.as_string())

    def close(self):
        self.server.close()

