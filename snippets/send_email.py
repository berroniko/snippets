import json
import smtplib
import ssl

from email.message import EmailMessage

with open("credentials.json") as f:
    credentials = json.load(f)

password = credentials['password']
sender = credentials['email']
host = credentials['host']


# Open the plain text file whose name is in textfile for reading.
# with open(textfile) as fp:
#     # Create a text/plain message
#     msg = EmailMessage()
#     msg.set_content(fp.read())

def send(recipient: str, subject: str, message: str):

    msg = EmailMessage()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.set_content(message)

    # Create a secure SSL context
    port = 465  # For SSL
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host=host, port=port, context=context) as server:
        server.login(sender, password)
        server.send_message(msg)


send(recipient="491729622430@mmsc.o2online.de", subject="from python recipient cell", message="test")