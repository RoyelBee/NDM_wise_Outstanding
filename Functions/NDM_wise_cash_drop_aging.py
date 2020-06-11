import Functions.all_function as fn
import Functions.all_library as lib


def ndm_cash_drop():
    ndm_anwar_cash_drop_df = lib.pd.read_sql_query(""" SELECT  AgingDays, sum(Amount)/1000 as Amount FROM (  Select
            case
                when Days_Diff between 0 and 3  THEN '0 - 3 days'
                when Days_Diff between 4 and 10  THEN '4 - 10 days'
                when Days_Diff between 11 and 15  THEN '11 - 15 days'
                else '16+ Days' end  as AgingDays,
            --OUT_NET
            Sum(OUT_NET) as Amount,
            CASE
                when TblCredit.Days_Diff between '0' and '3'  THEN 1
                when TblCredit.Days_Diff between '4' and '10'  THEN 2
                when TblCredit.Days_Diff between '11' and '15'  THEN 3
                ELSE  4
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
                        else '16+ Days' end
                ,CASE
                when TblCredit.Days_Diff between '0' and '3'  THEN 1
                when TblCredit.Days_Diff between '4' and '10'  THEN 2
                when TblCredit.Days_Diff between '11' and '15'  THEN 3
                ELSE 4 end ) as T1
                group by T1.AgingDays, SERIAL
            order by SERIAL """, fn.conn)
    anwar_cash_drop = ndm_anwar_cash_drop_df['Amount'].tolist()
    # print(anwar_cash_drop)
    ndm_kamrul_cash_drop_df = lib.pd.read_sql_query(""" SELECT  AgingDays, sum(Amount)/1000 as Amount FROM (  Select
            case
                when Days_Diff between 0 and 3  THEN '0 - 3 days'
                when Days_Diff between 4 and 10  THEN '4 - 10 days'
                when Days_Diff between 11 and 15  THEN '11 - 15 days'
                else '16+ Days' end  as AgingDays,
            --OUT_NET
            Sum(OUT_NET) as Amount,
            CASE
                when TblCredit.Days_Diff between '0' and '3'  THEN 1
                when TblCredit.Days_Diff between '4' and '10'  THEN 2
                when TblCredit.Days_Diff between '11' and '15'  THEN 3
                ELSE  4
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
                        else '16+ Days' end
                ,CASE
                when TblCredit.Days_Diff between '0' and '3'  THEN 1
                when TblCredit.Days_Diff between '4' and '10'  THEN 2
                when TblCredit.Days_Diff between '11' and '15'  THEN 3
                ELSE 4 end ) as T1
                group by T1.AgingDays, SERIAL
            order by SERIAL """, fn.conn)
    kamrul_cash_drop = ndm_kamrul_cash_drop_df['Amount'].tolist()
    # print(kamrul_cash_drop)
    ndm_atik_cash_drop_df = lib.pd.read_sql_query(""" SELECT  AgingDays, sum(Amount)/1000 as Amount FROM (  Select
            case
                when Days_Diff between 0 and 3  THEN '0 - 3 days'
                when Days_Diff between 4 and 10  THEN '4 - 10 days'
                when Days_Diff between 11 and 15  THEN '11 - 15 days'
                else '16+ Days' end  as AgingDays,
            --OUT_NET
            Sum(OUT_NET) as Amount,
            CASE
                when TblCredit.Days_Diff between '0' and '3'  THEN 1
                when TblCredit.Days_Diff between '4' and '10'  THEN 2
                when TblCredit.Days_Diff between '11' and '15'  THEN 3
                ELSE  4
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
                        else '16+ Days' end
                ,CASE
                when TblCredit.Days_Diff between '0' and '3'  THEN 1
                when TblCredit.Days_Diff between '4' and '10'  THEN 2
                when TblCredit.Days_Diff between '11' and '15'  THEN 3
                ELSE 4 end ) as T1
                group by T1.AgingDays, SERIAL
            order by SERIAL """, fn.conn)
    atik_cash_drop = ndm_atik_cash_drop_df['Amount'].tolist()
    # print(atik_cash_drop)
    ndm_nurul_cash_drop_df = lib.pd.read_sql_query(""" SELECT  AgingDays, sum(Amount)/1000 as Amount FROM (  Select
            case
                when Days_Diff between 0 and 3  THEN '0 - 3 days'
                when Days_Diff between 4 and 10  THEN '4 - 10 days'
                when Days_Diff between 11 and 15  THEN '11 - 15 days'
                else '16+ Days' end  as AgingDays,
            --OUT_NET
            Sum(OUT_NET) as Amount,
            CASE
                when TblCredit.Days_Diff between '0' and '3'  THEN 1
                when TblCredit.Days_Diff between '4' and '10'  THEN 2
                when TblCredit.Days_Diff between '11' and '15'  THEN 3
                ELSE  4
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
                        else '16+ Days' end
                ,CASE
                when TblCredit.Days_Diff between '0' and '3'  THEN 1
                when TblCredit.Days_Diff between '4' and '10'  THEN 2
                when TblCredit.Days_Diff between '11' and '15'  THEN 3
                ELSE 4 end ) as T1
                group by T1.AgingDays, SERIAL
            order by SERIAL """, fn.conn)
    nurul_cash_drop = ndm_nurul_cash_drop_df['Amount'].tolist()
    # print(nurul_cash_drop)
    ndm_hafizur_cash_drop_df = lib.pd.read_sql_query(""" SELECT  AgingDays, sum(Amount)/1000 as Amount FROM (  Select
            case
                when Days_Diff between 0 and 3  THEN '0 - 3 days'
                when Days_Diff between 4 and 10  THEN '4 - 10 days'
                when Days_Diff between 11 and 15  THEN '11 - 15 days'
                else '16+ Days' end  as AgingDays,
            --OUT_NET
            Sum(OUT_NET) as Amount,
            CASE
                when TblCredit.Days_Diff between '0' and '3'  THEN 1
                when TblCredit.Days_Diff between '4' and '10'  THEN 2
                when TblCredit.Days_Diff between '11' and '15'  THEN 3
                ELSE  4
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
                        else '16+ Days' end
                ,CASE
                when TblCredit.Days_Diff between '0' and '3'  THEN 1
                when TblCredit.Days_Diff between '4' and '10'  THEN 2
                when TblCredit.Days_Diff between '11' and '15'  THEN 3
                ELSE 4 end ) as T1
                group by T1.AgingDays, SERIAL
            order by SERIAL """, fn.conn)
    hafizur_cash_drop = ndm_hafizur_cash_drop_df['Amount'].tolist()
    # print(hafizur_cash_drop)
    bar_one_lebel_array = [(anwar_cash_drop[0] / sum(anwar_cash_drop)) * 100,
                           (anwar_cash_drop[1] / sum(anwar_cash_drop)) * 100,
                           (anwar_cash_drop[2] / sum(anwar_cash_drop)) * 100,
                           (anwar_cash_drop[3] / sum(anwar_cash_drop)) * 100]

    bar_two_lebel_array = [(kamrul_cash_drop[0] / sum(kamrul_cash_drop)) * 100,
                           (kamrul_cash_drop[1] / sum(kamrul_cash_drop)) * 100,
                           (kamrul_cash_drop[2] / sum(kamrul_cash_drop)) * 100,
                           (kamrul_cash_drop[3] / sum(kamrul_cash_drop)) * 100]

    bar_three_lebel_array = [(atik_cash_drop[0] / sum(atik_cash_drop)) * 100,
                             (atik_cash_drop[1] / sum(atik_cash_drop)) * 100,
                             (atik_cash_drop[2] / sum(atik_cash_drop)) * 100,
                             (atik_cash_drop[3] / sum(atik_cash_drop)) * 100]
    bar_four_lebel_array = [(nurul_cash_drop[0] / sum(nurul_cash_drop)) * 100,
                            (nurul_cash_drop[1] / sum(nurul_cash_drop)) * 100,
                            (nurul_cash_drop[2] / sum(nurul_cash_drop)) * 100,
                            (nurul_cash_drop[3] / sum(nurul_cash_drop)) * 100]

    bar_five_lebel_array = [(hafizur_cash_drop[0] / sum(hafizur_cash_drop)) * 100,
                            (hafizur_cash_drop[1] / sum(hafizur_cash_drop)) * 100,
                            (hafizur_cash_drop[2] / sum(hafizur_cash_drop)) * 100,
                            (hafizur_cash_drop[3] / sum(hafizur_cash_drop)) * 100]
    N = 4
    y_pos = lib.np.arange(N)
    # print(y_pos)
    bar_width = .12
    fig, ax = lib.plt.subplots(figsize=(12.8, 4.8))
    rects1 = lib.plt.bar(y_pos + 0.00, bar_one_lebel_array, width=bar_width, align='center', alpha=0.9, color='#1a58c5')
    rects2 = lib.plt.bar(y_pos + 0.12, bar_two_lebel_array, width=bar_width, align='center', alpha=0.9, color='#be4748')
    rects3 = lib.plt.bar(y_pos + 0.24, bar_three_lebel_array, width=bar_width, align='center', alpha=0.9,
                         color='#c5871a')
    rects4 = lib.plt.bar(y_pos + 0.36, bar_four_lebel_array, width=bar_width, align='center', alpha=0.9,
                         color='#58c51a')
    rects5 = lib.plt.bar(y_pos + 0.48, bar_five_lebel_array, width=bar_width, align='center', alpha=0.9,
                         color='#fc0373')

    def autolabel1(rects):
        q = 0
        for rect in rects:
            val = bar_one_lebel_array[q]
            h = rect.get_height()
            ax.text(rect.get_x() + rect.get_width() / 2., 1.01 * h, '%.2f' % val + '%',
                    ha='center', va='bottom', rotation=90,fontweight='bold')
            q = q + 1

    autolabel1(rects1)

    def autolabel2(rects):
        q = 0
        for rect in rects:
            val = bar_two_lebel_array[q]
            h = rect.get_height()
            ax.text(rect.get_x() + rect.get_width() / 2., 1.01 * h, '%.2f' % val + '%',
                    ha='center', va='bottom', rotation=90,fontweight='bold')
            q = q + 1

    autolabel2(rects2)

    def autolabel3(rects):
        q = 0
        for rect in rects:
            val = bar_three_lebel_array[q]
            h = rect.get_height()
            ax.text(rect.get_x() + rect.get_width() / 2., 1.01 * h, '%.2f' % val + '%',
                    ha='center', va='bottom', rotation=90,fontweight='bold')
            q = q + 1

    autolabel3(rects3)

    def autolabel4(rects):
        q = 0
        for rect in rects:
            val = bar_four_lebel_array[q]
            h = rect.get_height()
            ax.text(rect.get_x() + rect.get_width() / 2., 1.01 * h, '%.2f' % val + '%',
                    ha='center', va='bottom', rotation=90,fontweight='bold')
            q = q + 1

    autolabel4(rects4)

    def autolabel5(rects):
        q = 0
        for rect in rects:
            val = bar_five_lebel_array[q]
            h = rect.get_height()
            ax.text(rect.get_x() + rect.get_width() / 2., 1.01 * h, '%.2f' % val + '%',
                    ha='center', va='bottom', rotation=90,fontweight='bold')
            q = q + 1

    autolabel5(rects5)
    max_amount = max(kamrul_cash_drop)
    labels = ['A- 0 t0 3 days', 'B- 4 to 10 days', 'C- 11 to 15 days', 'D- 16+ days']
    lib.plt.xticks(y_pos, labels, rotation='horizontal', fontsize='12')
    lib.plt.yticks(lib.np.arange(0, 101, 10), fontsize='12')
    lib.plt.title("11. NDM Wise Cash Drop Aging", fontsize=16, fontweight='bold', color='#3e0a75')
    lib.plt.legend(['Mr. Anwar', 'Mr. Kamrul', 'Mr. Atik', 'Mr. Nurul', 'Mr. Hafizur'])
    lib.plt.tight_layout()
    # lib.plt.show()
    lib.plt.savefig('./Images/11.ndm_cash_drop_aging.png')
    print('11. NDM wise cash drop aging')
