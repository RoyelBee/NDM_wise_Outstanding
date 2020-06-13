import pandas as pd
import pyodbc as db
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import numpy as np
from datetime import datetime
import smtplib
import os
import csv

conn = db.connect('DRIVER={SQL Server};'
                        'SERVER=137.116.139.217;'
                        'DATABASE=ARCHIVESKF;'
                        'UID=sa;PWD=erp@123')

dirpath = os.path.dirname(os.path.realpath(__file__))

aging_mature_df = pd.read_sql_query("""
            SELECT  AgingDays, sum(Amount)/1000 as Amount FROM
            (Select
            case
            when TblCredit.Days_Diff between '0' and '3'  THEN '0 - 3 days'
            when TblCredit.Days_Diff between '4' and '10'  THEN '4 - 10 days'
            when TblCredit.Days_Diff between '11' and '15'  THEN '11 - 15 days'
            when TblCredit.Days_Diff between '16' and '30'  THEN '16 - 30 days'
            when TblCredit.Days_Diff between '31' and '90'  THEN '31 - 90 days'
            when TblCredit.Days_Diff between '91' and '201'  THEN '91 - 201 days'

            else '202+ Days' end  as AgingDays,
            --OUT_NET
            Sum(OUT_NET) as Amount,

            CASE
            when TblCredit.Days_Diff between '1' and '3'  THEN 1
            when TblCredit.Days_Diff between '4' and '10'  THEN 2
            when TblCredit.Days_Diff between '11' and '15'  THEN 3
            when TblCredit.Days_Diff between '16' and '30'  THEN 4
            when TblCredit.Days_Diff between '31' and '90'  THEN 5
            when TblCredit.Days_Diff between '91' and '201' THEN 6

            ELSE  7
            END AS SERIAL
            from
            (select INVNUMBER,INVDATE,
            CUSTOMER,TERMS,MAINCUSTYPE,
            CustomerInformation.CREDIT_LIMIT_DAYS,
            (datediff([dd] , CONVERT (DATETIME , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1-CREDIT_LIMIT_DAYS) as Days_Diff,
            OUT_NET from [ARCOUT].dbo.[CUST_OUT]
            join ARCHIVESKF.dbo.CustomerInformation
            on [CUST_OUT].CUSTOMER = CustomerInformation.IDCUST
            where TERMS<>'Cash' ) as TblCredit
            where Days_Diff>0

            group by
            case
            when TblCredit.Days_Diff between '0' and '3'  THEN '0 - 3 days'
            when TblCredit.Days_Diff between '4' and '10'  THEN '4 - 10 days'
            when TblCredit.Days_Diff between '11' and '15'  THEN '11 - 15 days'
            when TblCredit.Days_Diff between '16' and '30'  THEN '16 - 30 days'
            when TblCredit.Days_Diff between '31' and '90'  THEN '31 - 90 days'
            when TblCredit.Days_Diff between '91' and '201'  THEN '91 - 201 days'
            else '202+ Days' end,
            CASE
            when TblCredit.Days_Diff between '1' and '3'  THEN 1
            when TblCredit.Days_Diff between '4' and '10'  THEN 2
            when TblCredit.Days_Diff between '11' and '15'  THEN 3
            when TblCredit.Days_Diff between '16' and '30'  THEN 4
            when TblCredit.Days_Diff between '31' and '90'  THEN 5
            when TblCredit.Days_Diff between '91' and '201' THEN 6

            ELSE  7
            END ) AS T1
            group by T1.AgingDays, SERIAL
            order by SERIAL
                      """, conn)

#print(aging_mature_df)

aging_mature_df.to_csv (r'D:\Python Code\NDM_wise_Outstanding\matured_credit_aging.csv', index = False, header=True)

branch_wise_mature_credit_df = pd.read_sql_query(""" 
        SELECT left(TblCredit.AUDTORG, 3) as Branch, 
        isnull(SUM(case when Days_Diff between '0' and '3'  then OUT_NET end),0.1)  as '0 - 3 days',
        isnull(SUM(case when Days_Diff between '4' and '10' then OUT_NET end),0.1)  as '4 - 10 days',
        isnull(SUM(case when Days_Diff between '11' and '15' then OUT_NET end),0.1)  as '11 - 15 days',
        isnull(SUM(case when Days_Diff >= '16'  then OUT_NET end),0.1)  as '16+ days'

        from
        (
        select [CUST_OUT].INVNUMBER,
        [CUST_OUT].INVDATE, 
        [CUST_OUT].CUSTOMER,
        [CUST_OUT].TERMS,MAINCUSTYPE, 
        OesalesDetails.AUDTORG,
        CustomerInformation.CREDIT_LIMIT_DAYS,
        datediff([dd] , CONVERT (DATETIME , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1-CREDIT_LIMIT_DAYS as Days_Diff,
        OUT_NET from [ARCOUT].dbo.[CUST_OUT]
        join ARCHIVESKF.dbo.CustomerInformation
        on [CUST_OUT].CUSTOMER = CustomerInformation.IDCUST 
        join ARCHIVESKF.dbo.OESalesDetails on  OesalesDetails.CUSTOMER = CustomerInformation.IDCUST

        where [CUST_OUT].TERMS<>'Cash' and OUT_NET>0 and datediff([dd] , CONVERT (DATETIME , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1-CREDIT_LIMIT_DAYS>0
        group by [CUST_OUT].INVNUMBER,[CUST_OUT].INVDATE,[CUST_OUT].CUSTOMER, [CUST_OUT].TERMS,MAINCUSTYPE, OesalesDetails.AUDTORG,
        CustomerInformation.CREDIT_LIMIT_DAYS, OUT_NET 
        ) as TblCredit

        group by  TblCredit.AUDTORG
        order by TblCredit.AUDTORG
                    """, conn)

branch_wise_mature_credit_df.to_csv (r'D:\Python Code\NDM_wise_Outstanding\branch_wise_matured_credit_aging.csv', index = False, header=True)

branch_wise_non_matured_credit_aging_df= pd.read_sql_query(""" 
            SELECT left(TblCredit.AUDTORG, 3) as Branch, 
            isnull(SUM(case when TblCredit.Days_Diff between '-3' and '0'  THEN OUT_NET end), 0.1)  as '0 - 3 days',
            isnull(sum(case when TblCredit.Days_Diff between '-10' and '-4'  THEN OUT_NET end), 0.1) as  '4 - 10 days', 
            isnull(sum( case when TblCredit.Days_Diff between '-15' and '-11'  THEN OUT_NET end), 0.1) as '11 - 15 days', 
            isnull(sum(case when TblCredit.Days_Diff <='-16' THEN OUT_NET end), 0.1) as '16+ days'
            from (
            select [CUST_OUT].INVNUMBER,
            [CUST_OUT].INVDATE, 
            [CUST_OUT].CUSTOMER,
            [CUST_OUT].TERMS,MAINCUSTYPE, 
            OesalesDetails.AUDTORG,
            CustomerInformation.CREDIT_LIMIT_DAYS,
            datediff([dd] , CONVERT (DATETIME , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1-CREDIT_LIMIT_DAYS as Days_Diff,
            OUT_NET from [ARCOUT].dbo.[CUST_OUT]
            join ARCHIVESKF.dbo.CustomerInformation
            on [CUST_OUT].CUSTOMER = CustomerInformation.IDCUST 
            join ARCHIVESKF.dbo.OESalesDetails on  OesalesDetails.CUSTOMER = CustomerInformation.IDCUST

            where [CUST_OUT].TERMS<>'Cash' 

            and OUT_NET>0 
            and datediff([dd] , CONVERT (DATETIME , LTRIM(cust_out.INVDATE) , 102) 
            , GETDATE())+1-CREDIT_LIMIT_DAYS<0
            group by [CUST_OUT].INVNUMBER,[CUST_OUT].INVDATE,[CUST_OUT].CUSTOMER, [CUST_OUT].TERMS,MAINCUSTYPE, OesalesDetails.AUDTORG,
            CustomerInformation.CREDIT_LIMIT_DAYS, OUT_NET 
            ) as TblCredit

            group by  TblCredit.AUDTORG
            order by TblCredit.AUDTORG
                    """, conn)

branch_wise_non_matured_credit_aging_df.to_csv (r'D:\Python Code\NDM_wise_Outstanding\branch_wise_non_matured_credit_aging.csv', index = False, header=True)

branch_wise_cash_drop_aging_df =pd.read_sql_query("""
            SELECT left(TblCredit.AUDTORG, 3) as Branch, 
            isnull(SUM(case when Days_Diff between '0' and '3'  then OUT_NET end),0)  as '0 - 3 days',
            isnull(SUM(case when Days_Diff between '4' and '10' then OUT_NET end),0)  as '4 - 10 days',
            isnull(SUM(case when Days_Diff between '11' and '15' then OUT_NET end),0)  as '11 - 15 days',
            isnull(SUM(case when Days_Diff >= '16'  then OUT_NET end),0)  as '16+ days'

            from
            (select AUDTORG,INVNUMBER,INVDATE,
            CUSTOMER,TERMS,MAINCUSTYPE,
            datediff([dd] , CONVERT (DATETIME , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1 as Days_Diff,
            OUT_NET from [ARCOUT].dbo.[CUST_OUT]
            where TERMS='Cash') as TblCredit
            group by  TblCredit.AUDTORG
            order by TblCredit.AUDTORG  
                            """, conn)

branch_wise_cash_drop_aging_df.to_csv (r'D:\Python Code\NDM_wise_Outstanding\branch_wise_cash_drop_aging.csv', index = False, header=True)
