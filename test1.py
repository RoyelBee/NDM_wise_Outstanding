import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# ------------ Group email ----------------------------------------
msgRoot = MIMEMultipart('related')
me = 'erp-bi.service@transcombd.com'
to = ['fazle.rabby@transcombd.com','']
cc = ['', '']
bcc = ['', '']

recipient = to + cc + bcc

subject = "Test Report"

email_server_host = 'mail.transcombd.com'
port = 25

msgRoot['From'] = me

msgRoot['To'] = ', '.join(to)
msgRoot['Cc'] = ', '.join(cc)
msgRoot['Bcc'] = ', '.join(bcc)
msgRoot['Subject'] = subject

msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)

# msgText = MIMEText('This is the alternative plain text message.')
# msgAlternative.attach(msgText)

msgText = MIMEText("""
                       <img src="cid:img1_2" height='481', width='1281'><br>
                        <br>
                       """, 'html')

msgAlternative.attach(msgText)

# --------- Set Credit image in mail   -----------------------
fp = open('F:/test_picture/img1_2.png', 'rb')
img1_2 = MIMEImage(fp.read())
fp.close()

img1_2.add_header('Content-ID', '<img1_2>')
msgRoot.attach(img1_2)


# # ----------- Finally send mail and close server connection ---
server = smtplib.SMTP(email_server_host, port)
server.ehlo()
server.sendmail(me, recipient, msgRoot.as_string())
server.close()