import Functions.all_library as lib
import Functions.all_function as fn


def ndm_non_matured_credit_aging():
    anwar_df = lib.pd.read_sql_query("""
            SELECT  
           isnull(SUM(case when TblCredit.Days_Diff between '-3' and '0'  THEN OUT_NET end), 0.1)  as '0 - 3 days',
            isnull(sum(case when TblCredit.Days_Diff between '-10' and '-4'  THEN OUT_NET end), 0.1) as  '4 - 10 days', 
            isnull(sum( case when TblCredit.Days_Diff between '-15' and '-11'  THEN OUT_NET end), 0.1) as '11 - 15 days', 
            isnull(sum(case when TblCredit.Days_Diff between '-30' and '-16'  THEN OUT_NET end), 0.1) as '16 - 30 days', 
            isnull(sum(case when TblCredit.Days_Diff between '-90' and '-31'  THEN OUT_NET end), 0.1) as '31 - 90 days', 
            isnull(sum( case when TblCredit.Days_Diff between '-201' and '-91'  THEN OUT_NET end), 0.1) as '90 - 201 days', 
            isnull(sum( case when TblCredit.Days_Diff <= '-202'  THEN OUT_NET end), 0.1) as '202+ days'
            from
            (select CUSTNAME, INVNUMBER,INVDATE,
            CUSTOMER,TERMS,MAINCUSTYPE,
            CustomerInformation.CREDIT_LIMIT_DAYS,
            (datediff([dd] , CONVERT (DATETIME , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1-CREDIT_LIMIT_DAYS) as Days_Diff,
            OUT_NET from [ARCOUT].dbo.[CUST_OUT]
            join ARCHIVESKF.dbo.CustomerInformation
            on [CUST_OUT].CUSTOMER = CustomerInformation.IDCUST
            where [ARCOUT].dbo.[CUST_OUT].AUDTORG IN ('BOGSKF','MYMSKF', 'FRDSKF', 'TGLSKF', 'RAJSKF', 'SAVSKF') and 
            TERMS<>'Cash' and (datediff([dd] , CONVERT (DATETIME , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1-CREDIT_LIMIT_DAYS)<=0
            ) as TblCredit
                         """, fn.conn)

    anwar_0_3 = int(anwar_df['0 - 3 days'])
    anwar_4_10 = int(anwar_df['4 - 10 days'])
    anwar_11_15 = int(anwar_df['11 - 15 days'])
    anwar_16_30 = int(anwar_df['16 - 30 days'])
    anwar_31_90 = int(anwar_df['31 - 90 days'])
    anwar_91_201 = int(anwar_df['90 - 201 days'])
    anwar_202_more = int(anwar_df['202+ days'])

    # # -------------------------------------------------
    kamrul_df = lib.pd.read_sql_query("""
            SELECT  
            isnull(SUM(case when TblCredit.Days_Diff between '-3' and '0'  THEN OUT_NET end), 0.1)  as '0 - 3 days',
            isnull(sum(case when TblCredit.Days_Diff between '-10' and '-4'  THEN OUT_NET end), 0.1) as  '4 - 10 days', 
            isnull(sum( case when TblCredit.Days_Diff between '-15' and '-11'  THEN OUT_NET end), 0.1) as '11 - 15 days', 
            isnull(sum(case when TblCredit.Days_Diff between '-30' and '-16'  THEN OUT_NET end), 0.1) as '16 - 30 days', 
            isnull(sum(case when TblCredit.Days_Diff between '-90' and '-31'  THEN OUT_NET end), 0.1) as '31 - 90 days', 
            isnull(sum( case when TblCredit.Days_Diff between '-201' and '-91'  THEN OUT_NET end), 0.1) as '90 - 201 days', 
            isnull(sum( case when TblCredit.Days_Diff <= '-202'  THEN OUT_NET end), 0.1) as '202+ days'
            from
            (select CUSTNAME, INVNUMBER,INVDATE,
            CUSTOMER,TERMS,MAINCUSTYPE,
            CustomerInformation.CREDIT_LIMIT_DAYS,
            (datediff([dd] , CONVERT (DATETIME , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1-CREDIT_LIMIT_DAYS) as Days_Diff,
            OUT_NET from [ARCOUT].dbo.[CUST_OUT]
            join ARCHIVESKF.dbo.CustomerInformation
            on [CUST_OUT].CUSTOMER = CustomerInformation.IDCUST
            where [ARCOUT].dbo.[CUST_OUT].AUDTORG IN ('BSLSKF','COMSKF','JESSKF','KHLSKF','MIRSKF','PATSKF') and 
            TERMS<>'Cash' and (datediff([dd] , CONVERT (DATETIME , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1-CREDIT_LIMIT_DAYS)<=0
            ) as TblCredit

                    """, fn.conn)

    kamrul_0_3 = int(kamrul_df['0 - 3 days'])
    kamrul_4_10 = int(kamrul_df['4 - 10 days'])
    kamrul_11_15 = int(kamrul_df['11 - 15 days'])
    kamrul_16_30 = int(kamrul_df['16 - 30 days'])
    kamrul_31_90 = int(kamrul_df['31 - 90 days'])
    kamrul_91_201 = int(kamrul_df['90 - 201 days'])
    kamrul_202_more = int(kamrul_df['202+ days'])

    # # --------------------------------------------------
    atik_df = lib.pd.read_sql_query(""" 
           SELECT  
        isnull(SUM(case when TblCredit.Days_Diff between '-3' and '0'  THEN OUT_NET end), 0.1)  as '0 - 3 days',
            isnull(sum(case when TblCredit.Days_Diff between '-10' and '-4'  THEN OUT_NET end), 0.1) as  '4 - 10 days', 
            isnull(sum( case when TblCredit.Days_Diff between '-15' and '-11'  THEN OUT_NET end), 0.1) as '11 - 15 days', 
            isnull(sum(case when TblCredit.Days_Diff between '-30' and '-16'  THEN OUT_NET end), 0.1) as '16 - 30 days', 
            isnull(sum(case when TblCredit.Days_Diff between '-90' and '-31'  THEN OUT_NET end), 0.1) as '31 - 90 days', 
            isnull(sum( case when TblCredit.Days_Diff between '-201' and '-91'  THEN OUT_NET end), 0.1) as '90 - 201 days', 
            isnull(sum( case when TblCredit.Days_Diff <= '-202'  THEN OUT_NET end), 0.1) as '202+ days'
        from
        (select CUSTNAME, INVNUMBER,INVDATE,
        CUSTOMER,TERMS,MAINCUSTYPE,
        CustomerInformation.CREDIT_LIMIT_DAYS,
        (datediff([dd] , CONVERT (DATETIME , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1-CREDIT_LIMIT_DAYS) as Days_Diff,
        OUT_NET from [ARCOUT].dbo.[CUST_OUT]
        join ARCHIVESKF.dbo.CustomerInformation
        on [CUST_OUT].CUSTOMER = CustomerInformation.IDCUST
        where [ARCOUT].dbo.[CUST_OUT].AUDTORG IN ('DNJSKF','GZPSKF','HZJSKF','KRNSKF','KSGSKF','MOTSKF','RNGSKF') and 
        TERMS<>'Cash' and (datediff([dd] , CONVERT (DATETIME , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1-CREDIT_LIMIT_DAYS)<=0
        ) as TblCredit

                """, fn.conn)

    atik_0_3 = int(atik_df['0 - 3 days'])
    atik_4_10 = int(atik_df['4 - 10 days'])
    atik_11_15 = int(atik_df['11 - 15 days'])
    atik_16_30 = int(atik_df['16 - 30 days'])
    atik_31_90 = int(atik_df['31 - 90 days'])
    atik_91_201 = int(atik_df['90 - 201 days'])
    atik_202_more = int(atik_df['202+ days'])
    # # ---------------------------------------------
    nurul_df = lib.pd.read_sql_query("""
            SELECT  
           isnull(SUM(case when TblCredit.Days_Diff between '-3' and '0'  THEN OUT_NET end), 0.1)  as '0 - 3 days',
            isnull(sum(case when TblCredit.Days_Diff between '-10' and '-4'  THEN OUT_NET end), 0.1) as  '4 - 10 days', 
            isnull(sum( case when TblCredit.Days_Diff between '-15' and '-11'  THEN OUT_NET end), 0.1) as '11 - 15 days', 
            isnull(sum(case when TblCredit.Days_Diff between '-30' and '-16'  THEN OUT_NET end), 0.1) as '16 - 30 days', 
            isnull(sum(case when TblCredit.Days_Diff between '-90' and '-31'  THEN OUT_NET end), 0.1) as '31 - 90 days', 
            isnull(sum( case when TblCredit.Days_Diff between '-201' and '-91'  THEN OUT_NET end), 0.1) as '90 - 201 days', 
            isnull(sum( case when TblCredit.Days_Diff <= '-202'  THEN OUT_NET end), 0.1) as '202+ days'
            from
            (select CUSTNAME, INVNUMBER,INVDATE,
            CUSTOMER,TERMS,MAINCUSTYPE,
            CustomerInformation.CREDIT_LIMIT_DAYS,
            (datediff([dd] , CONVERT (DATETIME , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1-CREDIT_LIMIT_DAYS) as Days_Diff,
            OUT_NET from [ARCOUT].dbo.[CUST_OUT]
            join ARCHIVESKF.dbo.CustomerInformation
            on [CUST_OUT].CUSTOMER = CustomerInformation.IDCUST
            where [ARCOUT].dbo.[CUST_OUT].AUDTORG IN ('FENSKF','MHKSKF','MLVSKF','NOKSKF','SYLSKF','VRBSKF') and 
            TERMS<>'Cash' and (datediff([dd] , CONVERT (DATETIME , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1-CREDIT_LIMIT_DAYS)<=0
            ) as TblCredit

                            """, fn.conn)

    nurul_0_3 = int(nurul_df['0 - 3 days'])
    nurul_4_10 = int(nurul_df['4 - 10 days'])
    nurul_11_15 = int(nurul_df['11 - 15 days'])
    nurul_16_30 = int(nurul_df['16 - 30 days'])
    nurul_31_90 = int(nurul_df['31 - 90 days'])
    nurul_91_201 = int(nurul_df['90 - 201 days'])
    nurul_202_more = int(nurul_df['202+ days'])

    # # -------------------------------------------
    hafizur_df = lib.pd.read_sql_query("""
            SELECT  
            isnull(SUM(case when TblCredit.Days_Diff between '-3' and '0'  THEN OUT_NET end), 0.1)  as '0 - 3 days',
            isnull(sum(case when TblCredit.Days_Diff between '-10' and '-4'  THEN OUT_NET end), 0.1) as  '4 - 10 days', 
            isnull(sum( case when TblCredit.Days_Diff between '-15' and '-11'  THEN OUT_NET end), 0.1) as '11 - 15 days', 
            isnull(sum(case when TblCredit.Days_Diff between '-30' and '-16'  THEN OUT_NET end), 0.1) as '16 - 30 days', 
            isnull(sum(case when TblCredit.Days_Diff between '-90' and '-31'  THEN OUT_NET end), 0.1) as '31 - 90 days', 
            isnull(sum( case when TblCredit.Days_Diff between '-201' and '-91'  THEN OUT_NET end), 0.1) as '90 - 201 days', 
            isnull(sum( case when TblCredit.Days_Diff <= '-202'  THEN OUT_NET end), 0.1) as '202+ days'
            
            from
            (select CUSTNAME, INVNUMBER,INVDATE,
            CUSTOMER,TERMS,MAINCUSTYPE,
            CustomerInformation.CREDIT_LIMIT_DAYS,
            (datediff([dd] , CONVERT (DATETIME , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1-CREDIT_LIMIT_DAYS) as Days_Diff,
            OUT_NET from [ARCOUT].dbo.[CUST_OUT]
            join ARCHIVESKF.dbo.CustomerInformation
            on [CUST_OUT].CUSTOMER = CustomerInformation.IDCUST
            where [ARCOUT].dbo.[CUST_OUT].AUDTORG IN ('COXSKF','CTGSKF','CTNSKF','KUSSKF','NAJSKF','PBNSKF') and 
            TERMS<>'Cash' and (datediff([dd] , CONVERT (DATETIME , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1-CREDIT_LIMIT_DAYS)<=0
            ) as TblCredit

                                    """, fn.conn)

    hafizur_0_3 = int(hafizur_df['0 - 3 days'])
    hafizur_4_10 = int(hafizur_df['4 - 10 days'])
    hafizur_11_15 = int(hafizur_df['11 - 15 days'])
    hafizur_16_30 = int(hafizur_df['16 - 30 days'])
    hafizur_31_90 = int(hafizur_df['31 - 90 days'])
    hafizur_91_201 = int(hafizur_df['90 - 201 days'])
    hafizur_202_more = int(hafizur_df['202+ days'])
    # # Convert data into percentage
    anwar = [anwar_0_3, anwar_4_10, anwar_11_15, anwar_16_30, anwar_31_90, anwar_91_201, anwar_202_more]
    anwar = [i * 100 / sum(anwar) for i, j, in zip(anwar, anwar)]

    kamrul = [kamrul_0_3, kamrul_4_10, kamrul_11_15, kamrul_16_30, kamrul_31_90, kamrul_91_201, kamrul_202_more]
    kamrul = [i * 100 / sum(kamrul) for i, j, in zip(kamrul, kamrul)]

    atik = [atik_0_3, atik_4_10, atik_11_15, atik_16_30, atik_31_90, atik_91_201, atik_202_more]
    atik = [i * 100 / sum(atik) for i, j, in zip(atik, atik)]

    nurul = [nurul_0_3, nurul_4_10, nurul_11_15, nurul_16_30, nurul_31_90, nurul_91_201, nurul_202_more]
    nurul = [i * 100 / sum(nurul) for i, j, in zip(nurul, nurul)]

    hafizur = [hafizur_0_3, hafizur_4_10, hafizur_11_15, hafizur_16_30, hafizur_31_90, hafizur_91_201, hafizur_202_more]
    hafizur = [i * 100 / sum(hafizur) for i, j, in zip(hafizur, hafizur)]

    fig, ax = lib.plt.subplots(figsize=(12.81, 4.8))
    barWidth = .12
    x = lib.np.arange(7)

    legend_element = [lib.Patch(facecolor='#0093e6', label='Mr. Anwar'),
                      lib.Patch(facecolor='#e6a700', label='Mr. Kamrul'),
                      lib.Patch(facecolor='#dadde6', label='Mr. Atik'),
                      lib.Patch(facecolor='#f7ef03', label='Mr. Nurul'),
                      lib.Patch(facecolor='#85f703', label='Mr. Hafizur')
                      ]
    anwar_bar = lib.plt.bar(x + 0.00, anwar, color='#0093e6', label='Matured', edgecolor='white', width=barWidth)
    kamrul_bar = lib.plt.bar(x + 0.12, kamrul, color='#e6a700', label='Matured', edgecolor='white', width=barWidth)
    atik_bar = lib.plt.bar(x + 0.24, atik, color='#dadde6', label='Matured', edgecolor='white', width=barWidth)
    nurul_bar = lib.plt.bar(x + 0.36, nurul, color='#f7ef03', label='Matured', edgecolor='white', width=barWidth)
    hafizur_bar = lib.plt.bar(x + 0.48, hafizur, color='#85f703', label='Matured', edgecolor='white', width=barWidth)

    # # ------------ Add label in the top of the bar --------------------------
    for bar, anwar in zip(anwar_bar, anwar):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height*.9, str('%.1f' % height) + '%',
                ha='center', va='bottom', fontweight='bold', rotation=90)

    for bar, kamrul in zip(kamrul_bar, kamrul):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height*.9,  str('%.1f' % height) + '%',
                ha='center', va='bottom', fontweight='bold', rotation=90)

    for bar, atik in zip(atik_bar, atik):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height*.9,  str('%.1f' % height) + '%',
                ha='center', va='bottom', fontweight='bold', rotation=90)
    #
    for bar, nurul in zip(nurul_bar, nurul):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height*.9, str('%.1f' % height) + '%',
                ha='center', va='bottom', fontweight='bold', rotation=90)
    #
    for bar, hafizur in zip(hafizur_bar, hafizur):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height*.9, str('%.1f' % height) + '%',
                ha='center', va='bottom', fontweight='bold', rotation=90)

    # ------ Add legend elements -------------------

    category = ['0 to 3 Days', '4 to 10 Days', '11 to 15 Days', '16 to 30 Days', '31 to 90 Days', '91 to 201 Days',
                '202 to More']
    lib.plt.xticks(x + .25, category)

    lib.plt.title('8. NDM wise Non-Matured Credit Aging', fontsize=16, fontweight='bold', color='#3e0a75')
    lib.plt.legend(handles=legend_element, loc='best', fontsize=11)
    # return lib.plt.show()
    print('8. NDM non-matured credit Aging')
    return lib.plt.savefig('./Images/8.ndm_non_matured_credit_aging.png')
