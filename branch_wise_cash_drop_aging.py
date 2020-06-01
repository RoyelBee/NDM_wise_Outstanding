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


connection = db.connect('DRIVER={SQL Server};'
                        'SERVER=137.116.139.217;'
                        'DATABASE=ARCHIVESKF;'
                        'UID=sa;PWD=erp@123')

cursor = connection.cursor()

branch_cash_drop_df = pd.read_sql_query("""SELECT left(TblCredit.AUDTORG, 3) as Branch, 
isnull(SUM(case when Days_Diff between '0' and '3'  then OUT_NET end),0)  as '0 - 3 days',
isnull(SUM(case when Days_Diff between '4' and '10' then OUT_NET end),0)  as '4 - 10 days',
isnull(SUM(case when Days_Diff between '11' and '15' then OUT_NET end),0)  as '11 - 15 days',
isnull(SUM(case when Days_Diff between '16' and '30'  then OUT_NET end),0)  as '16 - 30 days',
isnull(SUM(case when Days_Diff between '31' and '90' then OUT_NET end),0)  as '31 - 90 days',
isnull(SUM(case when Days_Diff between '91' and '201' then OUT_NET end),0)  as '91 - 201 days'

        from
            (select AUDTORG,INVNUMBER,INVDATE,
            CUSTOMER,TERMS,MAINCUSTYPE,
            datediff([dd] , CONVERT (DATETIME , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1 as Days_Diff,
            OUT_NET from [ARCOUT].dbo.[CUST_OUT]
            where TERMS='Cash') as TblCredit
        group by  TblCredit.AUDTORG
		order by TblCredit.AUDTORG""", connection)


branch = branch_cash_drop_df['Branch']
zero_three = branch_cash_drop_df['0 - 3 days']
four_ten = branch_cash_drop_df['4 - 10 days']
eleven_fifteen = branch_cash_drop_df['11 - 15 days']
sixteen_therty = branch_cash_drop_df['16 - 30 days']
thrtyone_ninety = branch_cash_drop_df['31 - 90 days']
ninetyone_twohundredone = branch_cash_drop_df['91 - 201 days']

# # --------------------- Creating fig-----------------------------------------

# Data
r = np.arange(0, 31, 1)
print(r)

# # From raw value to percentage
totals = [i + j + k + l + m + n
          for i, j, k, l, m, n in zip(branch_cash_drop_df['0 - 3 days'],
                                         branch_cash_drop_df['4 - 10 days'],
                                         branch_cash_drop_df['11 - 15 days'],
                                         branch_cash_drop_df['16 - 30 days'],
                                         branch_cash_drop_df['31 - 90 days'],
                                         branch_cash_drop_df['91 - 201 days'])]

all_zero_three = [i / j * 100 for i, j in zip(branch_cash_drop_df['0 - 3 days'], totals)]
all_four_ten = [i / j * 100 for i, j in zip(branch_cash_drop_df['4 - 10 days'], totals)]
all_eleven_fifteen = [i / j * 100 for i, j in zip(branch_cash_drop_df['11 - 15 days'], totals)]
all_sixteen_therty = [i / j * 100 for i, j in zip(branch_cash_drop_df['16 - 30 days'], totals)]
all_thrtyone_ninety = [i / j * 100 for i, j in zip(branch_cash_drop_df['31 - 90 days'], totals)]
all_ninetyone_twohundredone = [i / j * 100 for i, j in zip(branch_cash_drop_df['91 - 201 days'], totals)]

# #
# plot
barWidth = 0.85
names = branch_cash_drop_df['Branch']
fig, ax = plt.subplots(figsize=(12.81, 9))
print(names)
#labels = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
labels=names.tolist()
def plot_stacked_bar(data, series_labels, category_labels=None,
                     show_values=False, value_format="{}", y_label=None,
                     colors=None, grid=False, reverse=False):
    """Plots a stacked bar chart with the data and labels provided.

    Keyword arguments:
    data            -- 2-dimensional numpy array or nested list
                       containing data for each series in rows
    series_labels   -- list of series labels (these appear in
                       the legend)
    category_labels -- list of category labels (these appear
                       on the x-axis)
    show_values     -- If True then numeric value labels will
                       be shown on each bar
    value_format    -- Format string for numeric value labels
                       (default is "{}")
    y_label         -- Label for y-axis (str)
    colors          -- List of color labels
    grid            -- If True display grid
    reverse         -- If True reverse the order that the
                       series are displayed (left-to-right
                       or right-to-left)
    """

    ny = len(data[0])
    ind = list(range(ny))

    axes = []
    cum_size = np.zeros(ny)

    data = np.array(data)

    if reverse:
        data = np.flip(data, axis=1)
        category_labels = reversed(category_labels)

    for i, row_data in enumerate(data):
        color = colors[i] if colors is not None else None
        axes.append(plt.bar(ind, row_data, bottom=cum_size,
                            label=series_labels[i], color=color))
        cum_size += row_data

    if category_labels:
        plt.xticks(ind, category_labels, rotation=90)

    if y_label:
        plt.ylabel(y_label)

    plt.legend()

    if grid:
        plt.grid()

    if show_values:
        for axis in axes:
            for bar in axis:
                w, h = bar.get_width(), bar.get_height()
                plt.text(bar.get_x() + w/2, bar.get_y() + h/2,
                         value_format.format(h), ha="center",
                         va="center", rotation=90)


#plt.figure(figsize=(12.81, 9))

series_labels = ['0 - 3 days', '4 - 10 days', '11 - 15 days', '16 - 30 days', '31 - 90 days', '91 - 201 days']

data = [
    all_zero_three,
    all_four_ten,
    all_eleven_fifteen,
    all_sixteen_therty,
    all_thrtyone_ninety,
    all_ninetyone_twohundredone
]

#category_labels = ['Cat A', 'Cat B', 'Cat C', 'Cat D']

plot_stacked_bar(
    data,
    series_labels,
    category_labels=labels,
    show_values=True,
    value_format='{:.0f}% ',
    colors=['#31c377','#f4b300','red','#96ff00','#0089ff','#e500ff','#00ffd8']
)

plt.xlabel("Branch Name", fontweight='bold', fontsize=12)
plt.ylabel("Percentage %", fontweight='bold', fontsize=12)
plt.title('Branch Wise Cash Drop', fontweight='bold', fontsize=16)
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.085),
          fancybox=True, shadow=True, ncol=7)
plt.show()
#plt.close()
print('done')