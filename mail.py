import smtplib


class Email():
    def __init__(self, gmail_user, gmail_password):
        self.server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        self.server.ehlo()
        self.server.login(gmail_user, gmail_password)

    def __enter__(self):
        return self.server

    def __exit__(self):
        self.server.close()

    def sendmail(self, _from, _to, subject, content):
        if type(_to) == str:
            _to = [_to]
        email_text = '''\
        From: %s
        To: %s
        Subject: %s

        %s
        ''' % (_from, ", ".join(_to), subject, content)
        self.server.sendmail(_from, _to, email_text)

    def close(self):
        self.server.close()
