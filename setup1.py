import smtplib
import os

from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from PIL import Image, ImageDraw, ImageFont
import Functions.all_library as lib

import generate_all_kpi
dirpath = os.path.dirname(os.path.realpath(__file__))

# # ----- Join Images --------------------------------------------
imp1 = Image.open(dirpath + "./Images/1.total_outstanding.png")
widthx, heightx = imp1.size
imp2 = Image.open(dirpath + "./Images/2.category_wise_credit.png")

imageSize = Image.new('RGB', (1283, 481))
imageSize.paste(imp1, (1, 0))
imageSize.paste(imp2, (widthx + 2, 0))
imageSize.save(dirpath + "./Images/img1_2.png")

# # Join 13, 14
imp13 = Image.open(dirpath + "./Images/13.Nation_wide_return.png")
imp14 = Image.open(dirpath + "./Images/14.nation_vs_ndm_return.png")
#
imageSize = Image.new('RGB', (1283, 301))
imageSize.paste(imp13, (1, 0))
imageSize.paste(imp14, (200 + 2, 0))
imageSize.save(dirpath + "./Images/img13_14.png")
print('Image joined ')
# -----------------------------------------------------------------
# ------------ Email Section --------------------------------------
# -----------------------------------------------------------------

# ------------ Group email ---------------------------------------
msgRoot = MIMEMultipart('related')
me = 'erp-bi.service@transcombd.com'
to = ['rejaul.islam@transcombd.com', '']
cc = ['', '']
bcc = ['', '']

recipient = to + cc + bcc

date = lib.datetime.today()
today = str(date.day) + '/' + str(date.month) + '/' + str(date.year) + ' ' + date.strftime("%I:%M %p")
subject = "SK+F Formulation Outstanding Reports " + today

email_server_host = 'mail.transcombd.com'
port = 25

msgRoot['From'] = me
# msgRoot['to'] = recipient
msgRoot['To'] = ', '.join(to)
msgRoot['Cc'] = ', '.join(cc)
msgRoot['Bcc'] = ', '.join(bcc)
msgRoot['Subject'] = subject

msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)

msgText = MIMEText('This is the alternative plain text message.')
msgAlternative.attach(msgText)

msgText = MIMEText("""
                       <img src="cid:img1_2" height='481', width='1281'><br>
                       <img src="cid:ndm_credit_outstanding" height='480', width='1280'><br>
                       <img src="cid:matured_credit_aging" height='480', width='1280'><br>
                       <img src="cid:ndm_matured_credit_aging" height='480', width='1280'><br>
                       <img src="cid:Branch_wise_matured_credit_aging" height='550', width='1280'><br>
                       <img src="cid:non_matured_credit_aging" height='550', width='1280'><br>
                       <img src="cid:ndm_non_matured_credit_aging" height='480', width='1280'><br>
                       <img src="cid:branch_non_matured" height='700', width='1280'><br>
                       <img src="cid:cashdrop_aging" height='480', width='1280'><br>
                       <img src="cid:ndm_cash_drop_aging" height='481', width='1281'><br>
                       <img src="cid:branch_wise_cash_drop_aging" height='481', width='1281'><br>
                       <img src="cid:img13_14" height='300', width='1281'><br>
                       <img src="cid:top5_branch_return" height='481', width='1281'><br>
                       <img src="cid:top5_delivery_persons_return" height='481', width='1281'><br>

                        <br>
                       """, 'html')

msgAlternative.attach(msgText)
# --------- Set Credit image in mail   -----------------------
fp = open(dirpath + './Images/img1_2.png', 'rb')
img1_2 = MIMEImage(fp.read())
fp.close()

img1_2.add_header('Content-ID', '<img1_2>')
msgRoot.attach(img1_2)

# # --------------------------------------------------------
fp = open(dirpath + './Images/3.ndm_credit_outstanding.png', 'rb')
ndm_credit_outstanding = MIMEImage(fp.read())
fp.close()

ndm_credit_outstanding.add_header('Content-ID', '<ndm_credit_outstanding>')
msgRoot.attach(ndm_credit_outstanding)


# # --------------------------------------------------------
fp = open(dirpath + './Images/4.matured_credit_aging.png', 'rb')
matured_credit_aging = MIMEImage(fp.read())
fp.close()

matured_credit_aging.add_header('Content-ID', '<matured_credit_aging>')
msgRoot.attach(matured_credit_aging)

# # --------------------------------------------------------
fp = open(dirpath + './Images/5.ndm_matured_credit_aging.png', 'rb')
ndm_matured_credit_aging = MIMEImage(fp.read())
fp.close()

ndm_matured_credit_aging.add_header('Content-ID', '<ndm_matured_credit_aging>')
msgRoot.attach(ndm_matured_credit_aging)

# # --------------------------------------------------------
fp = open(dirpath + './Images/6.Branch_wise_matured_credit_aging.png', 'rb')
Branch_wise_matured_credit_aging = MIMEImage(fp.read())
fp.close()

Branch_wise_matured_credit_aging.add_header('Content-ID', '<Branch_wise_matured_credit_aging>')
msgRoot.attach(Branch_wise_matured_credit_aging)


# # --------------------------------------------------------
fp = open(dirpath + './Images/7.non_matured_credit_aging.png', 'rb')
non_matured_credit_aging = MIMEImage(fp.read())
fp.close()

non_matured_credit_aging.add_header('Content-ID', '<non_matured_credit_aging>')
msgRoot.attach(non_matured_credit_aging)

# # --------------------------------------------------------
fp = open(dirpath + './Images/8.ndm_non_matured_credit_aging.png', 'rb')
ndm_non_matured_credit_aging = MIMEImage(fp.read())
fp.close()

ndm_non_matured_credit_aging.add_header('Content-ID', '<ndm_non_matured_credit_aging>')
msgRoot.attach(ndm_non_matured_credit_aging)

# # --------------------------------------------------------
fp = open(dirpath + './Images/9.branch_non_matured.png', 'rb')
branch_non_matured = MIMEImage(fp.read())
fp.close()

branch_non_matured.add_header('Content-ID', '<branch_non_matured>')
msgRoot.attach(branch_non_matured)

# # --------------------------------------------------------
fp = open(dirpath + './Images/10.cashdrop_aging.png', 'rb')
cashdrop_aging = MIMEImage(fp.read())
fp.close()

cashdrop_aging.add_header('Content-ID', '<cashdrop_aging>')
msgRoot.attach(cashdrop_aging)


# # --------------------------------------------------------
fp = open(dirpath + './Images/11.ndm_cash_drop_aging.png', 'rb')
ndm_cash_drop_aging = MIMEImage(fp.read())
fp.close()

ndm_cash_drop_aging.add_header('Content-ID', '<ndm_cash_drop_aging>')
msgRoot.attach(ndm_cash_drop_aging)


# # --------------------------------------------------------
fp = open(dirpath + './Images/12.branch_wise_cash_drop_aging.png', 'rb')
branch_wise_cash_drop_aging = MIMEImage(fp.read())
fp.close()

branch_wise_cash_drop_aging.add_header('Content-ID', '<branch_wise_cash_drop_aging>')
msgRoot.attach(branch_wise_cash_drop_aging)

# # --------------------------------------------------------
fp = open(dirpath + './Images/img13_14.png', 'rb')
img13_14 = MIMEImage(fp.read())
fp.close()

img13_14.add_header('Content-ID', '<img13_14>')
msgRoot.attach(img13_14)


# # --------------------------------------------------------
fp = open(dirpath + './Images/15.top5_branch_return.png', 'rb')
top5_branch_return = MIMEImage(fp.read())
fp.close()

top5_branch_return.add_header('Content-ID', '<top5_branch_return>')
msgRoot.attach(top5_branch_return)


# # --------------------------------------------------------
fp = open(dirpath + './Images/16.top5_delivery_persons_return.png', 'rb')
top5_delivery_persons_return = MIMEImage(fp.read())
fp.close()

top5_delivery_persons_return.add_header('Content-ID', '<top5_delivery_persons_return>')
msgRoot.attach(top5_delivery_persons_return)


# # ----------- Finally send mail and close server connection ---
server = smtplib.SMTP(email_server_host, port)
server.ehlo()
print('\n-----------------')
print('Sending Mail')
server.sendmail(me, recipient, msgRoot.as_string())
print('Mail Send')
print('-------------------')
server.close()
