import Functions.all_library as lib
import Functions.all_function as fn

anwar_df = lib.pd.read_sql_query("""
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
        where [ARCOUT].dbo.[CUST_OUT].AUDTORG IN ('BOGSKF','MYMSKF', 'FRDSKF', 'TGLSKF', 'RAJSKF', 'SAVSKF') and  TERMS<>'Cash' ) as TblCredit
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
                 """, fn.conn)

anwar_0_3 = int(anwar_df.Amount.loc[0])
anwar_4_10 = int(anwar_df.Amount.loc[1])
anwar_11_15 = int(anwar_df.Amount.loc[2])
anwar_16_30 = int(anwar_df.Amount.loc[3])
anwar_31_90 = int(anwar_df.Amount.loc[4])
anwar_91_201 = int(anwar_df.Amount.loc[5])
anwar_202_more = int(anwar_df.Amount.loc[6])

# # -------------------------------------------------
kamrul_df = lib.pd.read_sql_query("""
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
        where [ARCOUT].dbo.[CUST_OUT].AUDTORG IN ('BSLSKF','COMSKF','JESSKF','KHLSKF','MIRSKF','PATSKF') and  TERMS<>'Cash' ) as TblCredit
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
         
                """, fn.conn)

kamrul_0_3 = int(kamrul_df.Amount.loc[0])
kamrul_4_10 = int(kamrul_df.Amount.loc[1])
kamrul_11_15 = int(kamrul_df.Amount.loc[2])
kamrul_16_30 = int(kamrul_df.Amount.loc[3])
kamrul_31_90 = int(kamrul_df.Amount.loc[4])
kamrul_91_201 = int(kamrul_df.Amount.loc[5])
kamrul_202_more = int(kamrul_df.Amount.loc[6])

# # --------------------------------------------------
atik_df = lib.pd.read_sql_query(""" 
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
        where [ARCOUT].dbo.[CUST_OUT].AUDTORG IN ('DNJSKF','GZPSKF','HZJSKF','KRNSKF','KSGSKF','MOTSKF','RNGSKF') and  TERMS<>'Cash' ) as TblCredit
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
        
                        """, fn.conn)

atik_0_3 = int(atik_df.Amount.loc[0])
atik_4_10 = int(atik_df.Amount.loc[1])
atik_11_15 = int(atik_df.Amount.loc[2])
atik_16_30 = int(atik_df.Amount.loc[3])
atik_31_90 = int(atik_df.Amount.loc[4])
atik_91_201 = int(atik_df.Amount.loc[5])
atik_202_more = int(atik_df.Amount.loc[6])
# # ---------------------------------------------
nurul_df = lib.pd.read_sql_query("""
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
        where [ARCOUT].dbo.[CUST_OUT].AUDTORG IN ('FENSKF','MHKSKF','MLVSKF','NOKSKF','SYLSKF','VRBSKF') and  TERMS<>'Cash' ) as TblCredit
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
        
                        """, fn.conn)

nurul_0_3 = int(nurul_df.Amount.loc[0])
nurul_4_10 = int(nurul_df.Amount.loc[1])
nurul_11_15 = int(nurul_df.Amount.loc[2])
nurul_16_30 = int(nurul_df.Amount.loc[3])
nurul_31_90 = int(nurul_df.Amount.loc[4])
nurul_91_201 = int(nurul_df.Amount.loc[5])
nurul_202_more = int(nurul_df.Amount.loc[6])

# # -------------------------------------------
hafizur_df = lib.pd.read_sql_query("""
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
        where [ARCOUT].dbo.[CUST_OUT].AUDTORG IN ('COXSKF','CTGSKF','CTNSKF','KUSSKF','NAJSKF','PBNSKF') and  TERMS<>'Cash' ) as TblCredit
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
        
                                """, fn.conn)

hafizur_0_3 = int(hafizur_df.Amount.loc[0])
hafizur_4_10 = int(hafizur_df.Amount.loc[1])
hafizur_11_15 = int(hafizur_df.Amount.loc[2])
hafizur_16_30 = int(hafizur_df.Amount.loc[3])
hafizur_31_90 = int(hafizur_df.Amount.loc[4])
hafizur_91_201 = int(hafizur_df.Amount.loc[5])
hafizur_202_more = int(hafizur_df.Amount.loc[6])

# all_0_3 = [anwar_0_3, kamrul_0_3, atik_0_3, nurul_0_3, hafizur_0_3]
# all_4_10 = [anwar_4_10, kamrul_4_10, atik_4_10, nurul_4_10, hafizur_4_10]
# all_11_15 = [anwar_11_15, kamrul_11_15, atik_11_15, nurul_11_15, hafizur_11_15]
# all_16_30 = [anwar_16_30, kamrul_16_30, atik_16_30, nurul_16_30, hafizur_16_30]
# all_31_90 = [anwar_31_90, kamrul_31_90, atik_31_90, nurul_31_90, hafizur_31_90]
# all_91_201 = [anwar_91_201, kamrul_91_201, atik_91_201, nurul_91_201, hafizur_91_201]
# all_202_more = [anwar_202_more, kamrul_202_more, atik_202_more, nurul_202_more, hafizur_202_more]


data = {'all_0_3': [anwar_0_3, kamrul_0_3, atik_0_3, nurul_0_3, hafizur_0_3],
        'all_4_10': [anwar_4_10, kamrul_4_10, atik_4_10, nurul_4_10, hafizur_4_10],
        'all_11_15': [anwar_11_15, kamrul_11_15, atik_11_15, nurul_11_15, hafizur_11_15],
        'all_16_30': [anwar_16_30, kamrul_16_30, atik_16_30, nurul_16_30, hafizur_16_30],
        'all_31_90': [anwar_31_90, kamrul_31_90, atik_31_90, nurul_31_90, hafizur_31_90],
        'all_91_201': [anwar_91_201, kamrul_91_201, atik_91_201, nurul_91_201, hafizur_91_201],
        'all_202_more': [anwar_202_more, kamrul_202_more, atik_202_more, nurul_202_more, hafizur_202_more]}

df = lib.pd.DataFrame(data)
df.to_csv('ndm_matured_aging.csv', Index=False)
# print(df)

serial = [0, 1, 2, 3, 4, 5, 5]
name = ['0 to 3 Days', '4 to 10 Days', '11 to 15 Days', '16 to 30 Days', '31 to 90 Days', '91 to 201 Days', '202 to More']

totals = [i + j + k + l + m + n + o for i, j, k, l, m, n, o in
          zip(df['all_0_3'], df['all_4_10'], df['all_11_15'], df['all_16_30'], df['all_31_90'],
              df['all_91_201'], df['all_202_more'])]

all_0_3 = [i / j * 100 for i, j in zip(df['all_0_3'], totals)]
# all_4_10 = [i / j * 100 for i, j in zip(df['all_4_10'], totals)]
# all_11_15 = [i / j * 100 for i, j in zip(df['all_11_15'], totals)]
# all_16_30 = [i / j * 100 for i, j in zip(df['all_16_30'], totals)]
# all_31_90 = [i / j * 100 for i, j in zip(df['all_31_90'], totals)]
# all_91_201 = [i / j * 100 for i, j in zip(df['all_91_201'], totals)]
# all_202_more = [i / j * 100 for i, j in zip(df['all_202_more'], totals)]

barWidth = 0.80
bar1 = lib.plt.bar(serial, all_0_3, color='red', label='Matured', edgecolor='white', width=barWidth)
# Create orange Bars
# bar2 = lib.plt.bar(serial, all_4_10, bottom=all_0_3, color='blue', label='Non-Matured', edgecolor='white', width=barWidth)

lib.plt.show()
