
import Functions.all_library as lib
import Functions.all_function as fn


def branch_wise_non_matured_credit():
    data = lib.pd.read_sql_query(""" 
            SELECT left(TblCredit.AUDTORG, 3) as Branch, 
            isnull(SUM(case when TblCredit.Days_Diff between '-3' and '0'  THEN OUT_NET end), 0.1)  as '0 - 3 days',
            isnull(sum(case when TblCredit.Days_Diff between '-10' and '-4'  THEN OUT_NET end), 0.1) as  '4 - 10 days', 
            isnull(sum( case when TblCredit.Days_Diff between '-15' and '-11'  THEN OUT_NET end), 0.1) as '11 - 15 days', 
            isnull(sum(case when TblCredit.Days_Diff <='-16' THEN OUT_NET end), 0.1) as '16+ days'
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

    # # --------------------- Creating fig-----------------------------------------

    # Data
    r = lib.np.arange(0, 31, 1)

    # # From raw value to percentage

    totals = [i + j + k + l
              for i, j, k, l in zip(data['0 - 3 days'],
                                    data['4 - 10 days'],
                                    data['11 - 15 days'],
                                    data['16+ days'] )]

    all_zero_seven = [i / j * 100 for i, j in zip(data['0 - 3 days'], totals)]
    all_eight_fourteen = [i / j * 100 for i, j in zip(data['4 - 10 days'], totals)]
    all_fifteen_twentyone = [i / j * 100 for i, j in zip(data['11 - 15 days'], totals)]
    all_twentytwo_twentyeight = [i / j * 100 for i, j in zip(data['16+ days'], totals)]

    # #
    # plot
    barWidth = 0.85
    names = data['Branch']
    fig, ax = lib.plt.subplots(figsize=(12.8, 9))
    labels = names.tolist()

    def plot_stacked_bar(data, series_labels, category_labels=None,
                         show_values=False, value_format="{}", y_label=None,
                         colors=None, grid=False, reverse=False):

        ny = len(data[0])
        ind = list(range(ny))

        axes = []
        cum_size = lib.np.zeros(ny)

        data = lib.np.array(data)

        if reverse:
            data = lib.np.flip(data, axis=1)
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

    series_labels = ['0 - 3 days', '4 - 10 days', '11 - 15 days', '16+ days']
    data = [all_zero_seven, all_eight_fourteen, all_fifteen_twentyone, all_twentytwo_twentyeight]

    plot_stacked_bar(
        data,
        series_labels,
        category_labels=labels,
        show_values=True,
        value_format='{:.0f}% ',
        colors=['#e55025', '#f2ab97', '#dbed19', '#a9db11']
    )

    #lib.plt.xlabel("Branch Name", fontweight='bold', fontsize=12)
    lib.plt.ylabel("Percentage %", fontweight='bold', fontsize=12)
    lib.plt.title('9. Branch Wise Non-Matured Credit', fontsize=16, fontweight='bold', color='#3e0a75')
    lib.plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.085),
                   fancybox=True, shadow=True, ncol=7)

    lib.plt.savefig('./Images/9.branch_non_matured.png')
    print('9. Branch wise non-matured credit')
