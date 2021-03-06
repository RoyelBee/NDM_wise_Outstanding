import Functions.all_library as lib
import Functions.all_function as fn

def ndm_wise_outstanding():
    anwar_df = lib.pd.read_sql_query("""
            Select case when Days_Diff>0 then 'Matured Credit' else 'Regular Credit' End as  'Category',Sum(OUT_NET) as Amount from
            (select INVNUMBER,INVDATE,
            CUSTOMER,TERMS,MAINCUSTYPE,
            CustomerInformation.CREDIT_LIMIT_DAYS,
            datediff([dd] , CONVERT (DATETIME , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1-CREDIT_LIMIT_DAYS as Days_Diff,
            OUT_NET from [ARCOUT].dbo.[CUST_OUT]
            join ARCHIVESKF.dbo.CustomerInformation
            on [CUST_OUT].CUSTOMER = CustomerInformation.IDCUST
            where
            [ARCOUT].dbo.[CUST_OUT].AUDTORG IN ('BOGSKF','MYMSKF', 'FRDSKF', 'TGLSKF', 'RAJSKF', 'SAVSKF') and
             TERMS<>'Cash') as TblCredit
            group by case when Days_Diff>0 then 'Matured Credit' else 'Regular Credit' end """, fn.conn)

    anwar_matured = int(anwar_df.Amount.loc[0])
    anwar_regular = int(anwar_df.Amount.loc[1])

    # # -------------------------------------------------
    kamrul_df = lib.pd.read_sql_query("""
            Select case when Days_Diff>0 then 'Matured Credit' else 'Regular Credit' End as  'Category',Sum(OUT_NET) as Amount from
            (select INVNUMBER,INVDATE,
            CUSTOMER,TERMS,MAINCUSTYPE,
            CustomerInformation.CREDIT_LIMIT_DAYS,
            datediff([dd] , CONVERT (DATETIME , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1-CREDIT_LIMIT_DAYS as Days_Diff,
            OUT_NET from [ARCOUT].dbo.[CUST_OUT]
            join ARCHIVESKF.dbo.CustomerInformation
            on [CUST_OUT].CUSTOMER = CustomerInformation.IDCUST
            where
            [ARCOUT].dbo.[CUST_OUT].AUDTORG IN ('BSLSKF','COMSKF','JESSKF','KHLSKF','MIRSKF','PATSKF') and
             TERMS<>'Cash') as TblCredit
            group by case when Days_Diff>0 then 'Matured Credit' else 'Regular Credit' end
                    """, fn.conn)

    kamrul_matured = int(kamrul_df.Amount.loc[0])
    kamrul_regular = int(kamrul_df.Amount.loc[1])

    # # --------------------------------------------------
    atik_df = lib.pd.read_sql_query("""
            Select case when Days_Diff>0 then 'Matured Credit' else 'Regular Credit' End as  'Category',Sum(OUT_NET) as Amount from
            (select INVNUMBER,INVDATE,
            CUSTOMER,TERMS,MAINCUSTYPE,
            CustomerInformation.CREDIT_LIMIT_DAYS,
            datediff([dd] , CONVERT (DATETIME , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1-CREDIT_LIMIT_DAYS as Days_Diff,
            OUT_NET from [ARCOUT].dbo.[CUST_OUT]
            join ARCHIVESKF.dbo.CustomerInformation
            on [CUST_OUT].CUSTOMER = CustomerInformation.IDCUST
            where
            [ARCOUT].dbo.[CUST_OUT].AUDTORG IN ('DNJSKF','GZPSKF','HZJSKF','KRNSKF','KSGSKF','MOTSKF','RNGSKF') and
             TERMS<>'Cash') as TblCredit
            group by case when Days_Diff>0 then 'Matured Credit' else 'Regular Credit' end
                            """, fn.conn)

    atik_matured = int(atik_df.Amount.loc[0])
    atik_regular = int(atik_df.Amount.loc[1])

    # # ---------------------------------------------
    nurul_df = lib.pd.read_sql_query("""
            Select case when Days_Diff>0 then 'Matured Credit' else 'Regular Credit' End as  'Category',Sum(OUT_NET) as Amount from
            (select INVNUMBER,INVDATE,
            CUSTOMER,TERMS,MAINCUSTYPE,
            CustomerInformation.CREDIT_LIMIT_DAYS,
            datediff([dd] , CONVERT (DATETIME , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1-CREDIT_LIMIT_DAYS as Days_Diff,
            OUT_NET from [ARCOUT].dbo.[CUST_OUT]
            join ARCHIVESKF.dbo.CustomerInformation
            on [CUST_OUT].CUSTOMER = CustomerInformation.IDCUST
            where
            [ARCOUT].dbo.[CUST_OUT].AUDTORG IN ('FENSKF','MHKSKF','MLVSKF','NOKSKF','SYLSKF','VRBSKF') and
             TERMS<>'Cash') as TblCredit
            group by case when Days_Diff>0 then 'Matured Credit' else 'Regular Credit' end
                            """, fn.conn)

    nurul_matured = int(nurul_df.Amount.loc[0])
    nurul_regular = int(nurul_df.Amount.loc[1])

    # # -------------------------------------------
    hafizur_df = lib.pd.read_sql_query("""
            Select case when Days_Diff>0 then 'Matured Credit' else 'Regular Credit' End as  'Category',Sum(OUT_NET) as Amount from
            (select INVNUMBER,INVDATE,
            CUSTOMER,TERMS,MAINCUSTYPE,
            CustomerInformation.CREDIT_LIMIT_DAYS,
            datediff([dd] , CONVERT (DATETIME , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1-CREDIT_LIMIT_DAYS as Days_Diff,
            OUT_NET from [ARCOUT].dbo.[CUST_OUT]
            join ARCHIVESKF.dbo.CustomerInformation
            on [CUST_OUT].CUSTOMER = CustomerInformation.IDCUST
            where
            [ARCOUT].dbo.[CUST_OUT].AUDTORG IN ('COXSKF','CTGSKF','CTNSKF','KUSSKF','NAJSKF','PBNSKF') and
             TERMS<>'Cash') as TblCredit
            group by case when Days_Diff>0 then 'Matured Credit' else 'Regular Credit' end
                                    """, fn.conn)

    hafizur_matured = int(hafizur_df.Amount.loc[0])
    hafizur_regular = int(hafizur_df.Amount.loc[1])

    # # --------------------- Creating fig-----------------------------------------

    # Data
    r = [0, 1, 2, 3, 4]
    data = {'all_matured': [anwar_matured, kamrul_matured, atik_matured, nurul_matured, hafizur_matured],
            'all_regular': [anwar_regular, kamrul_regular, atik_regular, nurul_regular, hafizur_regular]}
    df = lib.pd.DataFrame(data)

    # From raw value to percentage
    totals = [i + j for i, j in zip(df['all_matured'], df['all_regular'])]
    all_matured = [i / j * 100 for i, j in zip(df['all_matured'], totals)]
    all_regular = [i / j * 100 for i, j in zip(df['all_regular'], totals)]
    # print('all matured = ', all_matured)

    # plot
    barWidth = 0.75
    names = ('Anwar', 'Kamrul', 'Atik', 'Nurul', 'Hafizur')

    fig, ax = lib.plt.subplots(figsize=(12.8, 4.8))
    bar1 = lib.plt.bar(r, all_matured, color='#b35e00', label='Matured', width=barWidth)
    bar2 = lib.plt.bar(r, all_regular, bottom=all_matured, color='#ffb667', label='Non-Matured',
                       width=barWidth)

    # # Set Matured Data Point
    matured = [anwar_matured, kamrul_matured, atik_matured, nurul_matured, hafizur_matured]
    for bar, matured, all_matured in zip(bar1, matured, all_matured):
        height = bar.get_height()
        # # This text is for actual matured data label
        ax.text(bar.get_x() + bar.get_width() / 2, height * .4,
                str(fn.numberInThousands(matured)),
                ha='center', va='bottom', fontweight='bold')

        # # This text is for percentage
        ax.text(bar.get_x() + bar.get_width() / 2, height * .2,
                str("%.2f" % all_matured) + '%',
                ha='center', va='bottom', color='white')

    # # Set Non Mature Data Point
    regular = [anwar_regular, kamrul_regular, atik_regular, nurul_regular, hafizur_regular]
    for bar, regular, all_regular in zip(bar2, regular, all_regular):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height * .8,
                str(fn.numberInThousands(regular)),
                ha='center', va='bottom', fontweight='bold')

        # # This text is for percentage
        ax.text(bar.get_x() + bar.get_width() / 2, height * .7,
                str("%.2f" % all_regular) + '%',
                ha='center', va='bottom', color='white')

    # Custom x axis
    lib.plt.xticks(r, names)
    # lib.plt.xlabel("NDM Name", fontweight='bold', fontsize=12)
    lib.plt.ylabel("Percentage %", fontweight='bold', fontsize=12)
    lib.plt.title('3. NDM wise Credit', fontsize=16, fontweight='bold', color='#3e0a75')
    lib.plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.065),
                   fancybox=True, shadow=True, ncol=4)
    print('3. NDM wise Credit Outstanding')
    lib.plt.savefig('./Images/3.ndm_credit_outstanding.png')
    # lib.plt.show()