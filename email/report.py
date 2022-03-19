# Send an HTML email with an embedded image and a plain text message for
# email clients that don't want to display the HTML.

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

# Define these once; use them twice!
strFrom = 'email0@email.com' # <<<<<<<<<<< EMAIL ORIGIN
strTo = 'email1@email.com, email2@email.com' # <<<<<<<< EMAIL DESTINATION

# Create the root message and fill in the from, to, and subject headers
msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = 'SUBJECT EMAIL' # <<<<<<<<<<<< SUBJECT EMAIL
msgRoot['From'] = strFrom
msgRoot['To'] = strTo
msgRoot.preamble = 'This is a multi-part message in MIME format.'

# Encapsulate the plain and HTML versions of the message body in an
# 'alternative' part, so message agents can decide which they want to display.
msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)

msgText = MIMEText('This is the alternative plain text message.')
msgAlternative.attach(msgText)

# We reference the image in the IMG SRC attribute by the ID we give it below
msgText = MIMEText('<b><center>TEXT EMAIL</center></b><br><img src="cid:image1"><br>', 'html') # <<<<<<<<<< YOUR EMAIL TEXT
msgAlternative.attach(msgText)

# This example assumes the image is in the current directory
fp = open('example.png', 'rb') # example: ('/home/user/example.png', 'rb') <<<<<<<<<<<< IMAGE DIRECTORY
msgImage = MIMEImage(fp.read())
fp.close()

# Define the image's ID as referenced above
msgImage.add_header('Content-ID', '<image1>')
msgRoot.attach(msgImage)

# Send the email (this example assumes SMTP authentication is required)
import smtplib
smtp = smtplib.SMTP('smtp.email.com', 25) # example: ('smtp.email.com', 25) <<<<<<<<< SMTP CONFIGURATION
smtp.ehlo()
smtp.starttls()
smtp.login('email@email.com.br', 'password') # example: ('email@email.com', 'password') <<<<<<<<<< SMTP CONFIGURATION
smtp.sendmail(strFrom, strTo, msgRoot.as_string())
smtp.quit()
