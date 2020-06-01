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

ndm_anwar_cash_drop_df = pd.read_sql_query(""" SELECT  AgingDays, sum(Amount)/1000 as Amount FROM (  Select
        case
            when Days_Diff between 0 and 3  THEN '0 - 3 days'
            when Days_Diff between 4 and 10  THEN '4 - 10 days'
            when Days_Diff between 11 and 15  THEN '11 - 15 days'
			when Days_Diff between 16 and 30  THEN '16 - 30 days'
			when Days_Diff between 31 and 90  THEN '31 - 90 days'
            else '90+ Days' end  as AgingDays,
        --OUT_NET
        Sum(OUT_NET) as Amount,

        CASE
            when TblCredit.Days_Diff between '0' and '3'  THEN 1
            when TblCredit.Days_Diff between '4' and '10'  THEN 2
            when TblCredit.Days_Diff between '11' and '15'  THEN 3
			when TblCredit.Days_Diff between '16' and '30'  THEN 4
            when TblCredit.Days_Diff between '31' and '90'  THEN 5
            ELSE  6
            END AS SERIAL
        from
            (select INVNUMBER,INVDATE,
            CUSTOMER,TERMS,MAINCUSTYPE,
            datediff([dd] , CONVERT (DATETIME , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1 as Days_Diff,
            OUT_NET from [ARCOUT].dbo.[CUST_OUT]
            where [ARCOUT].dbo.[CUST_OUT].AUDTORG IN ('BOGSKF','MYMSKF', 'FRDSKF', 'TGLSKF', 'RAJSKF', 'SAVSKF') and TERMS='Cash') as TblCredit
            group by

            case
                when Days_Diff between 0 and 3 THEN '0 - 3 days'
                when Days_Diff between 4 and 10  THEN '4 - 10 days'
                when Days_Diff between 11 and 15  THEN '11 - 15 days'
				when Days_Diff between 16 and 30  THEN '16 - 30 days'
			when Days_Diff between 31 and 90  THEN '31 - 90 days'
                    else '90+ Days' end
            ,CASE
            when TblCredit.Days_Diff between '0' and '3'  THEN 1
            when TblCredit.Days_Diff between '4' and '10'  THEN 2
            when TblCredit.Days_Diff between '11' and '15'  THEN 3
			when TblCredit.Days_Diff between '16' and '30'  THEN 4
            when TblCredit.Days_Diff between '31' and '90'  THEN 5
            ELSE 6 end ) as T1
            group by T1.AgingDays, SERIAL
        order by SERIAL """, connection)

anwar_cash_drop = ndm_anwar_cash_drop_df['Amount'].tolist()
print(anwar_cash_drop)

ndm_kamrul_cash_drop_df = pd.read_sql_query(""" SELECT  AgingDays, sum(Amount)/1000 as Amount FROM (  Select
        case
            when Days_Diff between 0 and 3  THEN '0 - 3 days'
            when Days_Diff between 4 and 10  THEN '4 - 10 days'
            when Days_Diff between 11 and 15  THEN '11 - 15 days'
			when Days_Diff between 16 and 30  THEN '16 - 30 days'
			when Days_Diff between 31 and 90  THEN '31 - 90 days'
            else '90+ Days' end  as AgingDays,
        --OUT_NET
        Sum(OUT_NET) as Amount,

        CASE
            when TblCredit.Days_Diff between '0' and '3'  THEN 1
            when TblCredit.Days_Diff between '4' and '10'  THEN 2
            when TblCredit.Days_Diff between '11' and '15'  THEN 3
			when TblCredit.Days_Diff between '16' and '30'  THEN 4
            when TblCredit.Days_Diff between '31' and '90'  THEN 5
            ELSE  6
            END AS SERIAL
        from
            (select INVNUMBER,INVDATE,
            CUSTOMER,TERMS,MAINCUSTYPE,
            datediff([dd] , CONVERT (DATETIME , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1 as Days_Diff,
            OUT_NET from [ARCOUT].dbo.[CUST_OUT]
            where [ARCOUT].dbo.[CUST_OUT].AUDTORG IN ('BSLSKF','COMSKF','JESSKF','KHLSKF','MIRSKF','PATSKF') and TERMS='Cash') as TblCredit
            group by

            case
                when Days_Diff between 0 and 3 THEN '0 - 3 days'
                when Days_Diff between 4 and 10  THEN '4 - 10 days'
                when Days_Diff between 11 and 15  THEN '11 - 15 days'
				when Days_Diff between 16 and 30  THEN '16 - 30 days'
			when Days_Diff between 31 and 90  THEN '31 - 90 days'
                    else '90+ Days' end
            ,CASE
            when TblCredit.Days_Diff between '0' and '3'  THEN 1
            when TblCredit.Days_Diff between '4' and '10'  THEN 2
            when TblCredit.Days_Diff between '11' and '15'  THEN 3
			when TblCredit.Days_Diff between '16' and '30'  THEN 4
            when TblCredit.Days_Diff between '31' and '90'  THEN 5
            ELSE 6 end ) as T1
            group by T1.AgingDays, SERIAL
        order by SERIAL """, connection)

kamrul_cash_drop = ndm_kamrul_cash_drop_df['Amount'].tolist()
print(kamrul_cash_drop)

ndm_atik_cash_drop_df = pd.read_sql_query(""" SELECT  AgingDays, sum(Amount)/1000 as Amount FROM (  Select
        case
            when Days_Diff between 0 and 3  THEN '0 - 3 days'
            when Days_Diff between 4 and 10  THEN '4 - 10 days'
            when Days_Diff between 11 and 15  THEN '11 - 15 days'
			when Days_Diff between 16 and 30  THEN '16 - 30 days'
			when Days_Diff between 31 and 90  THEN '31 - 90 days'
            else '90+ Days' end  as AgingDays,
        --OUT_NET
        Sum(OUT_NET) as Amount,

        CASE
            when TblCredit.Days_Diff between '0' and '3'  THEN 1
            when TblCredit.Days_Diff between '4' and '10'  THEN 2
            when TblCredit.Days_Diff between '11' and '15'  THEN 3
			when TblCredit.Days_Diff between '16' and '30'  THEN 4
            when TblCredit.Days_Diff between '31' and '90'  THEN 5
            ELSE  6
            END AS SERIAL
        from
            (select INVNUMBER,INVDATE,
            CUSTOMER,TERMS,MAINCUSTYPE,
            datediff([dd] , CONVERT (DATETIME , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1 as Days_Diff,
            OUT_NET from [ARCOUT].dbo.[CUST_OUT]
            where [ARCOUT].dbo.[CUST_OUT].AUDTORG IN ('DNJSKF','GZPSKF','HZJSKF','KRNSKF','KSGSKF','MOTSKF','RNGSKF') and TERMS='Cash') as TblCredit
            group by

            case
                when Days_Diff between 0 and 3 THEN '0 - 3 days'
                when Days_Diff between 4 and 10  THEN '4 - 10 days'
                when Days_Diff between 11 and 15  THEN '11 - 15 days'
				when Days_Diff between 16 and 30  THEN '16 - 30 days'
			when Days_Diff between 31 and 90  THEN '31 - 90 days'
                    else '90+ Days' end
            ,CASE
            when TblCredit.Days_Diff between '0' and '3'  THEN 1
            when TblCredit.Days_Diff between '4' and '10'  THEN 2
            when TblCredit.Days_Diff between '11' and '15'  THEN 3
			when TblCredit.Days_Diff between '16' and '30'  THEN 4
            when TblCredit.Days_Diff between '31' and '90'  THEN 5
            ELSE 6 end ) as T1
            group by T1.AgingDays, SERIAL
        order by SERIAL """, connection)

atik_cash_drop = ndm_atik_cash_drop_df['Amount'].tolist()
print(atik_cash_drop)

ndm_nurul_cash_drop_df = pd.read_sql_query(""" SELECT  AgingDays, sum(Amount)/1000 as Amount FROM (  Select
        case
            when Days_Diff between 0 and 3  THEN '0 - 3 days'
            when Days_Diff between 4 and 10  THEN '4 - 10 days'
            when Days_Diff between 11 and 15  THEN '11 - 15 days'
			when Days_Diff between 16 and 30  THEN '16 - 30 days'
			when Days_Diff between 31 and 90  THEN '31 - 90 days'
            else '90+ Days' end  as AgingDays,
        --OUT_NET
        Sum(OUT_NET) as Amount,

        CASE
            when TblCredit.Days_Diff between '0' and '3'  THEN 1
            when TblCredit.Days_Diff between '4' and '10'  THEN 2
            when TblCredit.Days_Diff between '11' and '15'  THEN 3
			when TblCredit.Days_Diff between '16' and '30'  THEN 4
            when TblCredit.Days_Diff between '31' and '90'  THEN 5
            ELSE  6
            END AS SERIAL
        from
            (select INVNUMBER,INVDATE,
            CUSTOMER,TERMS,MAINCUSTYPE,
            datediff([dd] , CONVERT (DATETIME , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1 as Days_Diff,
            OUT_NET from [ARCOUT].dbo.[CUST_OUT]
            where [ARCOUT].dbo.[CUST_OUT].AUDTORG IN ('FENSKF','MHKSKF','MLVSKF','NOKSKF','SYLSKF','VRBSKF') and TERMS='Cash') as TblCredit
            group by

            case
                when Days_Diff between 0 and 3 THEN '0 - 3 days'
                when Days_Diff between 4 and 10  THEN '4 - 10 days'
                when Days_Diff between 11 and 15  THEN '11 - 15 days'
				when Days_Diff between 16 and 30  THEN '16 - 30 days'
			when Days_Diff between 31 and 90  THEN '31 - 90 days'
                    else '90+ Days' end
            ,CASE
            when TblCredit.Days_Diff between '0' and '3'  THEN 1
            when TblCredit.Days_Diff between '4' and '10'  THEN 2
            when TblCredit.Days_Diff between '11' and '15'  THEN 3
			when TblCredit.Days_Diff between '16' and '30'  THEN 4
            when TblCredit.Days_Diff between '31' and '90'  THEN 5
            ELSE 6 end ) as T1
            group by T1.AgingDays, SERIAL
        order by SERIAL """, connection)

nurul_cash_drop = ndm_nurul_cash_drop_df['Amount'].tolist()
print(nurul_cash_drop)

ndm_hafizur_cash_drop_df = pd.read_sql_query(""" SELECT  AgingDays, sum(Amount)/1000 as Amount FROM (  Select
        case
            when Days_Diff between 0 and 3  THEN '0 - 3 days'
            when Days_Diff between 4 and 10  THEN '4 - 10 days'
            when Days_Diff between 11 and 15  THEN '11 - 15 days'
			when Days_Diff between 16 and 30  THEN '16 - 30 days'
			when Days_Diff between 31 and 90  THEN '31 - 90 days'
            else '90+ Days' end  as AgingDays,
        --OUT_NET
        Sum(OUT_NET) as Amount,

        CASE
            when TblCredit.Days_Diff between '0' and '3'  THEN 1
            when TblCredit.Days_Diff between '4' and '10'  THEN 2
            when TblCredit.Days_Diff between '11' and '15'  THEN 3
			when TblCredit.Days_Diff between '16' and '30'  THEN 4
            when TblCredit.Days_Diff between '31' and '90'  THEN 5
            ELSE  6
            END AS SERIAL
        from
            (select INVNUMBER,INVDATE,
            CUSTOMER,TERMS,MAINCUSTYPE,
            datediff([dd] , CONVERT (DATETIME , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1 as Days_Diff,
            OUT_NET from [ARCOUT].dbo.[CUST_OUT]
            where [ARCOUT].dbo.[CUST_OUT].AUDTORG IN ('COXSKF','CTGSKF','CTNSKF','KUSSKF','NAJSKF','PBNSKF') and TERMS='Cash') as TblCredit
            group by

            case
                when Days_Diff between 0 and 3 THEN '0 - 3 days'
                when Days_Diff between 4 and 10  THEN '4 - 10 days'
                when Days_Diff between 11 and 15  THEN '11 - 15 days'
				when Days_Diff between 16 and 30  THEN '16 - 30 days'
			when Days_Diff between 31 and 90  THEN '31 - 90 days'
                    else '90+ Days' end
            ,CASE
            when TblCredit.Days_Diff between '0' and '3'  THEN 1
            when TblCredit.Days_Diff between '4' and '10'  THEN 2
            when TblCredit.Days_Diff between '11' and '15'  THEN 3
			when TblCredit.Days_Diff between '16' and '30'  THEN 4
            when TblCredit.Days_Diff between '31' and '90'  THEN 5
            ELSE 6 end ) as T1
            group by T1.AgingDays, SERIAL
        order by SERIAL """, connection)

hafizur_cash_drop = ndm_hafizur_cash_drop_df['Amount'].tolist()
print(hafizur_cash_drop)

bar_one_lebel_array=[(anwar_cash_drop[0]/sum(anwar_cash_drop))*100,(anwar_cash_drop[1]/sum(anwar_cash_drop))*100,
                     (anwar_cash_drop[2]/sum(anwar_cash_drop))*100,(anwar_cash_drop[3]/sum(anwar_cash_drop))*100,
                     (anwar_cash_drop[4]/sum(anwar_cash_drop))*100,(anwar_cash_drop[5]/sum(anwar_cash_drop))*100]

bar_two_lebel_array=[(kamrul_cash_drop[0]/sum(kamrul_cash_drop))*100,(kamrul_cash_drop[1]/sum(kamrul_cash_drop))*100,
                     (kamrul_cash_drop[2]/sum(kamrul_cash_drop))*100,(kamrul_cash_drop[3]/sum(kamrul_cash_drop))*100,
                     (kamrul_cash_drop[4]/sum(kamrul_cash_drop))*100,(kamrul_cash_drop[5]/sum(kamrul_cash_drop))*100]
bar_three_lebel_array=[(atik_cash_drop[0]/sum(atik_cash_drop))*100,(atik_cash_drop[1]/sum(atik_cash_drop))*100,
                       (atik_cash_drop[2]/sum(atik_cash_drop))*100,(atik_cash_drop[3]/sum(atik_cash_drop))*100,
                       (atik_cash_drop[4]/sum(atik_cash_drop))*100,(atik_cash_drop[5]/sum(atik_cash_drop))*100]
bar_four_lebel_array=[(nurul_cash_drop[0]/sum(nurul_cash_drop))*100,(nurul_cash_drop[1]/sum(nurul_cash_drop))*100,
                      (nurul_cash_drop[2]/sum(nurul_cash_drop))*100,(nurul_cash_drop[3]/sum(nurul_cash_drop))*100,
                      (nurul_cash_drop[4]/sum(nurul_cash_drop))*100,(nurul_cash_drop[5]/sum(nurul_cash_drop))*100]
bar_five_lebel_array=[(hafizur_cash_drop[0]/sum(hafizur_cash_drop))*100,(hafizur_cash_drop[1]/sum(hafizur_cash_drop))*100,
                      (hafizur_cash_drop[2]/sum(hafizur_cash_drop))*100,(hafizur_cash_drop[3]/sum(hafizur_cash_drop))*100,
                      (hafizur_cash_drop[4]/sum(hafizur_cash_drop))*100,(hafizur_cash_drop[5]/sum(hafizur_cash_drop))*100]

N=6
y_pos = np.arange(N)
print(y_pos)

width=.15
fig, ax = plt.subplots(figsize=(12.81, 4.8))
rects1 = plt.bar(y_pos-width*2, bar_one_lebel_array,width=.15, align='center', alpha=0.9, color='blue')
rects2 = plt.bar(y_pos-width, bar_two_lebel_array,width=.15, align='center', alpha=0.9, color='orange')
rects3 = plt.bar(y_pos, bar_three_lebel_array,width=.15, align='center', alpha=0.9, color='grey')
rects4 = plt.bar(y_pos+width, bar_four_lebel_array,width=.15, align='center', alpha=0.9, color='yellow')
rects5 = plt.bar(y_pos+width+width, bar_five_lebel_array,width=.15, align='center', alpha=0.9, color='red')


def autolabel1(rects):
    q=0
    for rect in rects:
        val=bar_one_lebel_array[q]
        h = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.01*h, '%.2f'%val+'%',
                ha='center', va='bottom',rotation=90)
        q=q+1
autolabel1(rects1)

def autolabel2(rects):
    q=0
    for rect in rects:
        val=bar_two_lebel_array[q]
        h = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.01*h, '%.2f'%val+'%',
                ha='center', va='bottom',rotation=90)
        q=q+1
autolabel2(rects2)

def autolabel3(rects):
    q=0
    for rect in rects:
        val=bar_three_lebel_array[q]
        h = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.01*h, '%.2f'%val+'%',
                ha='center', va='bottom',rotation=90)
        q=q+1
autolabel3(rects3)

def autolabel4(rects):
    q=0
    for rect in rects:
        val=bar_four_lebel_array[q]
        h = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.01*h, '%.2f'%val+'%',
                ha='center', va='bottom',rotation=90)
        q=q+1
autolabel4(rects4)

def autolabel5(rects):
    q=0
    for rect in rects:
        val=bar_five_lebel_array[q]
        h = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.01*h, '%.2f'%val+'%',
                ha='center', va='bottom',rotation=90)
        q=q+1
autolabel5(rects5)


max_amount = max(kamrul_cash_drop)

labels=['A- 0 t0 3 days','B- 4 to 10 days','C- 11 to 15 days','D- 16 to 30 days','E- 31 to 90 days','F- 91 to 201 days']

plt.xticks(y_pos, labels, rotation='horizontal', fontsize='12')
plt.yticks(np.arange(0, 101,10), fontsize='12')
plt.title("15. NDM Wise Cash Drop Aging", color='#3e0a75', fontsize='16', fontweight='bold')
plt.legend(['Mr. Anwar','Mr. Kamrul','Mr. Atik','Mr. Nurul','Mr. Hafizur'])
plt.tight_layout()
plt.show()