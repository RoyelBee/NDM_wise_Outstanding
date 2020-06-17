import Functions.all_library as lib
import Functions.all_function as fn


def ndm_matured_credit_aging():
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
    # print(anwar_df)
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

    fig, ax = lib.plt.subplots(figsize=(12.8, 4.8))
    barWidth = .12
    x = lib.np.arange(7)

    legend_element = [
        lib.Patch(facecolor='#1a58c5', label='Mr. Anwar')
        , lib.Patch(facecolor='#be4748', label='Mr. Kamrul')
        , lib.Patch(facecolor='#c5871a', label='Mr. Atik')
        , lib.Patch(facecolor='#58c51a', label='Mr. Nurul')
        , lib.Patch(facecolor='#fc0373', label='Mr. Hafizur')]

    anwar_bar = lib.plt.bar(x + 0.00, anwar, color='#1a58c5', label='Matured', edgecolor='white', width=barWidth)
    kamrul_bar = lib.plt.bar(x + 0.12, kamrul, color='#be4748', label='Matured', edgecolor='white', width=barWidth)
    atik_bar = lib.plt.bar(x + 0.24, atik, color='#c5871a', label='Matured', edgecolor='white', width=barWidth)
    nurul_bar = lib.plt.bar(x + 0.36, nurul, color='#58c51a', label='Matured', edgecolor='white', width=barWidth)
    hafizur_bar = lib.plt.bar(x + 0.48, hafizur, color='#fc0373', label='Matured', edgecolor='white', width=barWidth)

    # # ------------ Add label in the top of the bar --------------------------
    for bar, anwar in zip(anwar_bar, anwar):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height * .92, str('%.1f' % height) + '%',
                ha='center', va='bottom', fontweight='bold', rotation=90)

    for bar, kamrul in zip(kamrul_bar, kamrul):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height * .92, str('%.1f' % height) + '%',
                ha='center', va='bottom', fontweight='bold', rotation=90)

    for bar, atik in zip(atik_bar, atik):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height * .92, str('%.1f' % height) + '%',
                ha='center', va='bottom', fontweight='bold', rotation=90)
    #
    for bar, nurul in zip(nurul_bar, nurul):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height * .92, str('%.1f' % height) + '%',
                ha='center', va='bottom', fontweight='bold', rotation=90)
    #
    for bar, hafizur in zip(hafizur_bar, hafizur):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height * .92, str('%.1f' % height) + '%',
                ha='center', va='bottom', fontweight='bold', rotation=90)

    # ------ Add legend elements -------------------

    category = ['0 to 3 Days', '4 to 10 Days', '11 to 15 Days', '16 to 30 Days', '31 to 90 Days', '91 to 201 Days',
                '202 to More']
    lib.plt.xticks(x + .25, category)

    lib.plt.title('5. NDM wise Matured Credit Aging', fontsize=16, fontweight='bold', color='#3e0a75')
    lib.plt.legend(handles=legend_element, loc='best', fontsize=11)
    lib.plt.tight_layout()
    # return lib.plt.show()

    print('5. NDM matured credit Aging')
    return lib.plt.savefig('./Images/5.ndm_matured_credit_aging.png')
