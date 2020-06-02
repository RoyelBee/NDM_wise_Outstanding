import pandas as pd
import numpy as np

import Functions.all_library as lib
import Functions.all_function as fn


def branch_wise_non_matured_credit():
    data = pd.read_sql_query(""" 
    SELECT left(TblCredit.AUDTORG, 3) as Branch, 
    isnull(SUM(case when TblCredit.Days_Diff between '-3' and '0'  THEN OUT_NET end), 0.1)  as '0 - 3 days',
    isnull(sum(case when TblCredit.Days_Diff between '-10' and '-4'  THEN OUT_NET end), 0.1) as  '4 - 10 days', 
    isnull(sum( case when TblCredit.Days_Diff between '-15' and '-11'  THEN OUT_NET end), 0.1) as '11 - 15 days', 
    isnull(sum(case when TblCredit.Days_Diff between '-30' and '-16'  THEN OUT_NET end), 0.1) as '16 - 30 days', 
    isnull(sum(case when TblCredit.Days_Diff between '-90' and '-31'  THEN OUT_NET end), .1) as '31 - 90 days', 
    isnull(sum( case when TblCredit.Days_Diff between '-201' and '-91'  THEN OUT_NET end), 0.1) as '91 - 201 days', 
    isnull(sum( case when TblCredit.Days_Diff >= '-202'  THEN OUT_NET end), 0) as '202+ days'
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
    order by TblCredit.AUDTORG
            """, fn.conn)

    # branch = data['Branch']
    # zero_three = data['0 - 3 days']
    # four_ten = data['4 - 10 days']
    # eleven_fifteen = data['11 - 15 days']
    # sixteen_therty = data['16 - 30 days']
    # thrtyone_ninety = data['31 - 90 days']
    # ninetyone_twohundredone = data['91 - 201 days']
    # twohundredtwo_more = data['202+ days']

    # # --------------------- Creating fig-----------------------------------------

    # Data
    r = np.arange(0, 31, 1)

    # # From raw value to percentage
    totals = [i + j + k + l + m + n + o
              for i, j, k, l, m, n, o in zip(data['0 - 3 days'],
                                             data['4 - 10 days'],
                                             data['11 - 15 days'],
                                             data['16 - 30 days'],
                                             data['31 - 90 days'],
                                             data['91 - 201 days'],
                                             data['202+ days'])]

    all_zero_three = [i / j * 100 for i, j in zip(data['0 - 3 days'], totals)]
    all_four_ten = [i / j * 100 for i, j in zip(data['4 - 10 days'], totals)]
    all_eleven_fifteen = [i / j * 100 for i, j in zip(data['11 - 15 days'], totals)]
    all_sixteen_therty = [i / j * 100 for i, j in zip(data['16 - 30 days'], totals)]
    all_thrtyone_ninety = [i / j * 100 for i, j in zip(data['31 - 90 days'], totals)]
    all_ninetyone_twohundredone = [i / j * 100 for i, j in zip(data['91 - 201 days'], totals)]
    all_twohundredtwo_more = [i / j * 100 for i, j in zip(data['202+ days'], totals)]

    # #
    # plot
    barWidth = 0.85
    names = data['Branch']
    fig, ax = lib.plt.subplots(figsize=(12.81, 9))
    # print(names)
    # labels = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
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
            for axis in axes:
                for bar in axis:
                    w, h = bar.get_width(), bar.get_height()
                    lib.plt.text(bar.get_x() + w / 2, bar.get_y() + h / 2,
                                 value_format.format(h), ha="center",
                                 va="center", rotation=90)

    lib.plt.figure(figsize=(12.81, 9))

    series_labels = ['0 - 3 days', '4 - 10 days', '11 - 15 days', '16 - 30 days', '31 - 90 days', '91 - 201 days', '202+ days']

    data = [
        all_zero_three,
        all_four_ten,
        all_eleven_fifteen,
        all_sixteen_therty,
        all_thrtyone_ninety,
        all_ninetyone_twohundredone,
        all_twohundredtwo_more
    ]

    # category_labels = ['Cat A', 'Cat B', 'Cat C', 'Cat D']

    plot_stacked_bar(
        data,
        series_labels,
        category_labels=labels,
        show_values=True,
        value_format='{:.0f}% ',
        colors=['#31c377', '#f4b300', 'red', '#96ff00', '#0089ff', '#e500ff', '#00ffd8']
    )

    lib.plt.xlabel("Branch Name", fontweight='bold', fontsize=12)
    lib.plt.ylabel("Percentage %", fontweight='bold', fontsize=12)
    lib.plt.title('Branch Wise Non-Matured Credit', fontweight='bold', fontsize=12)
    lib.plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.085),
                   fancybox=True, shadow=True, ncol=7)

    lib.plt.savefig('./Images/9.branch_non_matured.png')
    print('9. Branch wise non-matured credit')


