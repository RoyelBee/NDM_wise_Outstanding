from Functions import all_library as lib
import Functions.all_function as fn

import os

dirpath = os.path.dirname(os.path.realpath(__file__))

import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from math import log, floor
import matplotlib.patches as patches
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pyodbc as db
import xlrd
from matplotlib.patches import Patch
from PIL import Image, ImageDraw, ImageFont
import pytz
import datetime as dd
from PIL import Image
from datetime import datetime
import sys

def banner():
    date = datetime.today()
    day = str(date.day) + '/' + str(date.month) + '/' + str(date.year)
    tz_NY = pytz.timezone('Asia/Dhaka')
    datetime_BD = datetime.now(tz_NY)
    time = datetime_BD.strftime("%I:%M %p")
    date = datetime.today()
    x = dd.datetime.now()
    day = str(date.day) + '-' + str(x.strftime("%b")) + '-' + str(date.year)
    print(date)
    print(day)
    tz_NY = pytz.timezone('Asia/Dhaka')
    datetime_BD = datetime.now(tz_NY)
    time = datetime_BD.strftime("%I:%M %p")
    print(datetime_BD)
    print(time)
    img = Image.open("./Functions/new_ai.png")
    title = ImageDraw.Draw(img)
    timestore = ImageDraw.Draw(img)
    tag = ImageDraw.Draw(img)
    branch = ImageDraw.Draw(img)
    font = ImageFont.truetype("./Functions/Stencil_Regular.ttf", 60, encoding="unic")
    font1 = ImageFont.truetype("./Functions/ROCK.ttf", 50, encoding="unic")
    font2 = ImageFont.truetype("./Functions/ROCK.ttf", 35, encoding="unic")



    tag.text((25, 8), 'SK+F', (255, 255, 255), font=font)
    #branch.text((25, 270), branch_name + " Branch", (255, 209, 0), font=font1)
    timestore.text((25, 435), time + "\n" + day, (255, 255, 255), font=font2)
    img.save('./Functions/banner_ai.png')

    print('banner created')