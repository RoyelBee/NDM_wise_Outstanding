import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import Functions.all_library as lib
import Functions.all_function as fn


def branch_wise_non_matured_credit():
    data = lib.pd.read_sql_query(""" 
            SELECT left(TblCredit.AUDTORG, 3) as Branch, 
            isnull(SUM(case when TblCredit.Days_Diff between '-3' and '0'  THEN OUT_NET end), 0.1)/1000  as '0 - 3 days',
            isnull(sum(case when TblCredit.Days_Diff between '-10' and '-4'  THEN OUT_NET end), 0.1)/1000 as  '4 - 10 days', 
            isnull(sum( case when TblCredit.Days_Diff between '-15' and '-11'  THEN OUT_NET end), 0.1)/1000 as '11 - 15 days', 
            isnull(sum(case when TblCredit.Days_Diff <='-16' THEN OUT_NET end), 0.1)/1000 as '16+ days'
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
            order by sum(OUT_NET) desc
                    """, fn.conn)

    zeroTothree = data['0 - 3 days'].values.tolist()
    fourToten = data['4 - 10 days'].values.tolist()
    elevenTofifteen = data['11 - 15 days'].values.tolist()
    sixteenplus = data['16+ days'].values.tolist()

    branch_names = data['Branch'].values.tolist()

    result_list = []
    for p, q, r, s in zip(zeroTothree, fourToten, elevenTofifteen, sixteenplus):
        list1 = [p, q, r, s]
        result_list.append(list1)
    # print(result_list)

    totals = [i + j + k + l
              for i, j, k, l in zip(data['0 - 3 days'],
                                    data['4 - 10 days'],
                                    data['11 - 15 days'],
                                    data['16+ days'])]
    all_zero_seven = [i / j * 100 for i, j in zip(data['0 - 3 days'], totals)]
    all_eight_fourteen = [i / j * 100 for i, j in zip(data['4 - 10 days'], totals)]
    all_fifteen_twentyone = [i / j * 100 for i, j in zip(data['11 - 15 days'], totals)]
    all_twentytwo_twentyeight = [i / j * 100 for i, j in zip(data['16+ days'], totals)]

    max_value = max(totals)

    label_list = []
    for t, u, v, w in zip(all_zero_seven, all_eight_fourteen, all_fifteen_twentyone, all_twentytwo_twentyeight):
        list2 = [t, u, v, w]
        label_list.append(list2)
    # print(label_list)

    category_names = ['0 - 3 days', '4 - 10 days',
                      '11 - 15 days', '16+ days']
    results = result_list

    def survey(results, category_names):
        labels = branch_names
        data = np.array(results)
        width_data = np.array(label_list)
        data_cum = data.cumsum(axis=1)
        # category_colors = plt.get_cmap('RdYlGn')(
        #     np.linspace(0.15, 0.85, data.shape[1]))
        category_colors =['#e55025', '#f2ab97', '#dbed19', '#a9db11']
        fig, ax = plt.subplots(figsize=(12.8, 9))
        ax.invert_yaxis()
        ax.xaxis.set_visible(False)
        ax.set_xlim(0, np.sum(data, axis=1).max())

        for i, (colname, color) in enumerate(zip(category_names, category_colors)):
            widths = data[:, i]
            # print(widths)
            main_width = width_data[:, i]
            # print(main_width)
            starts = data_cum[:, i] - widths
            ax.barh(labels, widths, left=starts, height=.7,
                    label=colname, color=color)
            xcenters = starts + widths / 2

            #r, g, b, _ = color
            text_color = 'black'  # if r * g * b < 0.5 else 'darkgrey'
            for y, (x, c) in enumerate(zip(xcenters, main_width)):
                ax.text(x, y, str(round(c, 1)) + '%', ha='center', va='center',fontsize=8,
                        color=text_color)
        # ax.legend(ncol=len(category_names), bbox_to_anchor=(0, 1),
        #           loc='lower center', fontsize='small')
        #plt.xticks(np.arange(0, max_value, 10), fontsize='9')
        plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.025),
                   fancybox=True, shadow=True, ncol=7)
        plt.title('9. Branch Wise Non-Matured Credit', fontsize=16, fontweight='bold', color='#3E0A75')
        plt.tight_layout()

        return fig, ax

    survey(results, category_names)


    # plt.show()
    plt.savefig('./Images/9.branch_non_matured.png')
    print('9. Updated Branch wise non-matured credit')
