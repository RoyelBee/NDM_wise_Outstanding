import pandas as pd
import numpy as np
from collections import Iterable
import Functions.all_library as lib
import Functions.all_function as fn


def branch_wise_matured_credit():
    data = pd.read_sql_query("""
        SELECT left(TblCredit.AUDTORG, 3) as Branch,
isnull(SUM(case when Days_Diff between '0' and '3'  then OUT_NET end),0.1)/1000  as '0 - 3 days',
isnull(SUM(case when Days_Diff between '4' and '10' then OUT_NET end),0.1)/1000  as '4 - 10 days',
isnull(SUM(case when Days_Diff between '11' and '15' then OUT_NET end),0.1)/1000  as '11 - 15 days',
isnull(SUM(case when Days_Diff >= '16'  then OUT_NET end),0.1)/1000  as '16+ days', 
sum(OUT_NET) as 'All'
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
order by sum(OUT_NET) desc
                            """, fn.conn)
    data.to_csv(r'./Data/branch_wise_matured_credit_aging.csv', index=False, header=True)
    # # --------------------- Creating fig-----------------------------------------
    zeroTothree = data['0 - 3 days'].values.tolist()
    fourToten = data['4 - 10 days'].values.tolist()
    elevenTofifteen = data['11 - 15 days'].values.tolist()
    sixteenplus = data['16+ days'].values.tolist()
    print(zeroTothree)
    print(fourToten)
    print(elevenTofifteen)
    print(sixteenplus)
    # Data
    r = np.arange(0, 31, 1)
    # print(r)
    # # From raw value to percentage
    totals = [i + j + k + l
              for i, j, k, l in zip(data['0 - 3 days'],
                                    data['4 - 10 days'],
                                    data['11 - 15 days'],
                                    data['16+ days'])]
    all_zero_seven = [i / j * 100 for i, j in zip(data['0 - 3 days'], totals)]
    all_eight_fourteen = [i / j * 100 for i, j in zip(data['4 - 10 days'], totals)]
    all_fifteen_twentyone = [i / j * 100 for i, j in zip(data['11 - 15 days'], totals)]
    all_twentytwo_twentyeight = [i / j * 100 for i, j in zip(data['16+ days'], totals)]
    label_data = [all_zero_seven, all_eight_fourteen, all_fifteen_twentyone, all_twentytwo_twentyeight]
    print(label_data)

    def flatten(x):
        result = []
        for el in x:
            if hasattr(el, "__iter__") and not isinstance(el, str):
                result.extend(flatten(el))
            else:
                result.append(el)
        return result

    main_label = flatten(label_data)
    print(main_label)
    # plot
    barWidth = 0.85
    names = data['Branch']
    lib.plt.subplots(figsize=(12.8, 9))
    labels = names.tolist()

    def plot_stacked_bar(data, series_labels, category_labels=None,
                         show_values=False, value_format="{}", y_label=None,
                         colors=None, grid=False, reverse=False):
        ny = len(data[0])
        ind = list(range(ny))
        axes = []
        cum_size = np.zeros(ny)
        data = np.array(data)
        if reverse:
            data = np.flip(data, axis=1)
            category_labels = reversed(category_labels)
        for i, row_data in enumerate(data):
            color = colors[i] if colors is not None else None
            axes.append(lib.plt.bar(ind, row_data, bottom=cum_size,
                                    label=series_labels[i], color=color))
            cum_size += row_data
        if category_labels:
            lib.plt.xticks(ind, category_labels, rotation=90)
        if y_label:
            lib.plt.ylabel(y_label)
        lib.plt.legend()
        if grid:
            lib.plt.grid()
        if show_values:
            i = 0
            for axis in axes:
                for bar in axis:
                    w, h = bar.get_width(), bar.get_height()
                    lib.plt.text(bar.get_x() + w / 2, bar.get_y() + h / 2,
                                 value_format.format(float(main_label[i])), ha="center",
                                 va="center", rotation=90)
                    i = i + 1

    series_labels = ['0 - 3 days', '4 - 10 days', '11 - 15 days', '16+ days']
    data = [zeroTothree, fourToten, elevenTofifteen, sixteenplus]
    plot_stacked_bar(
        data,
        series_labels,
        category_labels=labels,
        show_values=True,
        value_format='{:.0f}% ',
        colors=['#31C377', '#F4B300', 'red', '#96FF00', '#0089FF', '#E500FF', '#00FFD8']
    )
    # lib.plt.xlabel("Branch Name", fontweight='bold', fontsize=12)
    lib.plt.ylabel("Amount(In Thousand)", fontweight='bold', fontsize=12)
    lib.plt.title('6. Branch Wise Matured Credit', fontsize=16, fontweight='bold', color='#3E0A75')
    lib.plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.085),
                   fancybox=True, shadow=True, ncol=7)
    # lib.plt.show()
    # plt.close()
    lib.plt.savefig('./Images/6.Branch_wise_matured_credit_aging.png')
    print('6. Branch wise matured credit aging')
