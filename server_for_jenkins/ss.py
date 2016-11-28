import smtplib
import email.utils
from email.mime.text import MIMEText

import socket

def send_mail(body, to, subject):
    msg = MIMEText(body)

    msg['To'] = email.utils.formataddr(('Recipient', to))
    msg['From'] = email.utils.formataddr(('Author', 'author@example.com'))
    msg['Subject'] = subject

    try:

        server = smtplib.SMTP(to)

    except socket.gaierror:
        print 'fail to send to', to
        return
    except socket.error:
        print 'fail to send to', to
        return
    except smtplib.SMTPServerDisconnected:
        print 'fail to send to', to
        return

    server.set_debuglevel(True) # show communication with the server
    try:
        server.sendmail('hello', [to], msg.as_string())

    finally:
        server.quit()

if __name__ == '__main__':

    send_mail('word', '10.8.130.180:8888', '[Urgent]')
    send_mail('word', '10.8.130.180:8', '[Urgent]') # IOError
    send_mail('word', '10130.180:8', '[Urgent]') # IOError
    send_mail('word', '10.8.130.180:8899', '[Urgent]') # IOError
