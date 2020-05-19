
import Functions.all_library as lib
import Functions.all_function as fn
query = """ SELECT  
        isnull(SUM(case when TblCredit.Days_Diff between '-3' and '0'  THEN OUT_NET end), 0)  as '0 - 3 days',
        isnull(sum(case when TblCredit.Days_Diff between '-10' and '-4'  THEN OUT_NET end), 0) as  '4 - 10 days', 
        isnull(sum( case when TblCredit.Days_Diff between '-15' and '-11'  THEN OUT_NET end), 0) as '11 - 15 days', 
        isnull(sum(case when TblCredit.Days_Diff between '-16' and '-30'  THEN OUT_NET end), 0) as '16 - 30 days', 
        isnull(sum(case when TblCredit.Days_Diff between '-31' and '-90'  THEN OUT_NET end), 0) as '31 - 90 days', 
        isnull(sum( case when TblCredit.Days_Diff between '-91' and '-201'  THEN OUT_NET end), 0) as '90 - 201 days', 
        isnull(sum( case when TblCredit.Days_Diff >= '-202'  THEN OUT_NET end), 0) as '202+ days'
        from
        (select CUSTNAME, INVNUMBER,INVDATE,
        CUSTOMER,TERMS,MAINCUSTYPE,
        CustomerInformation.CREDIT_LIMIT_DAYS,
        (datediff([dd] , CONVERT (DATETIME , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1-CREDIT_LIMIT_DAYS) as Days_Diff,
        OUT_NET from [ARCOUT].dbo.[CUST_OUT]
        join ARCHIVESKF.dbo.CustomerInformation
        on [CUST_OUT].CUSTOMER = CustomerInformation.IDCUST
        where --[ARCOUT].dbo.[CUST_OUT].AUDTORG like ? and 
        TERMS<>'Cash' and (datediff([dd] , CONVERT (DATETIME , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1-CREDIT_LIMIT_DAYS)<=0
        ) as TblCredit
        
        """


