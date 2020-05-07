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
