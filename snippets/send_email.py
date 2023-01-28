# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.message import EmailMessage

# Open the plain text file whose name is in textfile for reading.
# with open(textfile) as fp:
#     # Create a text/plain message
#     msg = EmailMessage()
#     msg.set_content(fp.read())

msg = EmailMessage()
msg.set_content("the message body")

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = f'Message from python'
msg['From'] = niko.kresse@googlemail.com
msg['To'] = mail.kresse@yahoo.de

# Send the message via our own SMTP server.
s = smtplib.SMTP('localhost')
s.send_message(msg)
s.quit()