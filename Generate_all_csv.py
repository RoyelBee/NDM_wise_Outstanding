import Functions.all_library as lib
import Functions.all_function as fn

def All_csv_generator():
    matured_credit_aging_df = lib.pd.read_sql_query("""
            SELECT   AUDTORG as [Branch Name],
            INVNUMBER as [Invoice Number] , INVDATE as [Invoice Date], CUSTOMER as [Customer ID], 
            CUSTNAME as [Customer Name],TEXTSTRE1 as [Address],  
            SUM(case when Days_Diff between '0' and '3'  then OUT_NET end)  as '0 - 3 days'
            , SUM(case when Days_Diff between '4' and '10'  then OUT_NET end)  as '4 - 10 days'
            , SUM(case when Days_Diff between '11' and '15'  then OUT_NET end)  as '11 - 15 days'
            , SUM(case when Days_Diff between '16' and '30'  then OUT_NET end)  as '16 - 30 days'
            , SUM(case when Days_Diff between '31' and '90'  then OUT_NET end)  as '31 - 90 days'
            , SUM(case when Days_Diff between '91' and '201'  then OUT_NET end)  as '91 - 201 days'
            , SUM(case when Days_Diff >='202'  then OUT_NET end)  as '202+ days'
            from
            (select INVNUMBER,INVDATE,CustomerInformation.AUDTORG,
            CUSTOMER,CUSTNAME,TEXTSTRE1, TERMS,MAINCUSTYPE,
            CustomerInformation.CREDIT_LIMIT_DAYS,
            (datediff([dd] , CONVERT (DATETIME , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1-CREDIT_LIMIT_DAYS) as Days_Diff,
            OUT_NET from [ARCOUT].dbo.[CUST_OUT]
            join ARCHIVESKF.dbo.CustomerInformation
            on [CUST_OUT].CUSTOMER = CustomerInformation.IDCUST
            where TERMS<>'Cash' ) as TblCredit
            --where  '0 - 3 days' IS NOT NULL
            group by INVNUMBER, INVDATE, CUSTOMER, CUSTNAME, TEXTSTRE1, AUDTORG
            ORDER BY INVDATE DESC, AUDTORG asc""", fn.conn)

    matured_credit_aging=matured_credit_aging_df.dropna(thresh=7)
    #print(matured_credit_aging)
    matured_credit_aging.to_csv(r'./Data/matured_credit_aging.csv', index=False, header=True)

    branch_wise_non_matured_credit_aging_df = lib.pd.read_sql_query("""
        SELECT
        left(TblCredit.AUDTORG, 3) as [Branch Name],
        INVNUMBER as [Invoice Number] , INVDATE as [Invoice Date], CUSTOMER as [Customer ID]
        , NAMECUST
        ,TEXTSTRE1 as [Address],
        SUM(case when TblCredit.Days_Diff between '-3' and '0'  THEN OUT_NET end)  as '0 - 3 days',
        sum(case when TblCredit.Days_Diff between '-10' and '-4'  THEN OUT_NET end) as  '4 - 10 days',
        sum( case when TblCredit.Days_Diff between '-15' and '-11'  THEN OUT_NET end) as '11 - 15 days',
        sum(case when TblCredit.Days_Diff <='-16' THEN OUT_NET end) as '16+ days'
        from (
        select [CUST_OUT].INVNUMBER,
        [CUST_OUT].INVDATE,
        [CUST_OUT].CUSTOMER,
        CustomerInformation.NAMECUST,
        CustomerInformation.TEXTSTRE1,
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
        group by [CUST_OUT].INVNUMBER,[CUST_OUT].INVDATE,[CUST_OUT].CUSTOMER, [CUST_OUT].TERMS,MAINCUSTYPE, OesalesDetails.AUDTORG,NAMECUST,
        CustomerInformation.CREDIT_LIMIT_DAYS, OUT_NET , TEXTSTRE1
        ) as TblCredit
        group by  TblCredit.AUDTORG, INVNUMBER, INVDATE , CUSTOMER,NAMECUST, TEXTSTRE1
        order by TblCredit.AUDTORG
            """, fn.conn)

    branch_wise_non_matured_credit_aging = branch_wise_non_matured_credit_aging_df.dropna(thresh=4)
    #print(branch_wise_non_matured_credit_aging)
    branch_wise_non_matured_credit_aging.to_csv(r'./Data/branch_wise_non_matured_credit_aging.csv', index=False, header=True)

    branch_wise_cash_drop_aging_df = lib.pd.read_sql_query("""
            SELECT left( AUDTORG, 3) as [Branch Name]
            ,INVNUMBER as [Invoice Number ],INVDATE as [Invoice Date],
            CUSTOMER as [Customer ID],CUSTNAME as [Customer Name],
            SUM(case when TblCredit.Days_Diff between '0' and '3'  THEN OUT_NET end)  as '0 - 3 days',
            SUM(case when TblCredit.Days_Diff between '4' and '10'  THEN OUT_NET end)  as '4 - 10 days',
            SUM(case when TblCredit.Days_Diff between '11' and '15'  THEN OUT_NET end)  as '11 - 15 days',
            SUM(case when TblCredit.Days_Diff >='202'  THEN OUT_NET end)  as '16+ days'
            from
            (select AUDTORG, INVNUMBER,INVDATE,
            CUSTOMER,CUSTNAME, TERMS,MAINCUSTYPE,
            datediff([dd] , CONVERT (DATETIME , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1 as Days_Diff,
            OUT_NET from [ARCOUT].dbo.[CUST_OUT]
            where TERMS='Cash') as TblCredit
            group by AUDTORG, INVNUMBER,INVDATE, CUSTOMER, CUSTNAME
            order by AUDTORG asc, INVDATE desc, '0 - 3 days' desc""", fn.conn)

    branch_wise_cash_drop_aging = branch_wise_cash_drop_aging_df.dropna(thresh=4)
    # print(branch_wise_non_matured_credit_aging)
    branch_wise_cash_drop_aging.to_csv(r'./Data/branch_wise_cash_drop_aging.csv', index=False, header=True)

    all_return_df = lib.pd.read_sql_query("""
                select AUDTORG, sales.DPID, DPNAME.DPNAME, 
                SUM(case when TRANSTYPE=1 then EXTINVMISC END) as SalesValus
                ,SUM(case when TRANSTYPE=2 then EXTINVMISC END)*-1 as ReturnValus
                , ((SUM(case when TRANSTYPE=2 then EXTINVMISC END)*-1)/SUM(case when TRANSTYPE=1 then EXTINVMISC END))*100 as ReturnPer
                --sum(EXTINVMISC)*-1 as ReturnValue 
                from (
                select AUDTORG, DPID, TRANSTYPE, EXTINVMISC from OESalesDetails
                where left(TRANSDATE,6)>=convert(varchar(6),getdate(),112)) as Sales
                left join
                (select DPID, DPNAME from DP_ShortName) as DPNAME
                on sales.DPID=DPNAME.DPID
                where DPNAME.DPNAME is not null
                group by AUDTORG, sales.DPID, DPNAME.DPNAME
                Having ISNULL(SUM(case when TRANSTYPE=1 then EXTINVMISC END),0) <>0 
                order by ReturnPer desc """, fn.conn)

    all_return = all_return_df.dropna()
    # print(branch_wise_non_matured_credit_aging)
    all_return.to_csv(r'./Data/all_return.csv', index=False, header=True)

    print('all csv generated')