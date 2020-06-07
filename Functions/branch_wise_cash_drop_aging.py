import Functions.all_library as lib
import Functions.all_function as fn

def branch_wise_cash_drop_aging():
    branch_cash_drop_df = lib.pd.read_sql_query("""
            SELECT left(TblCredit.AUDTORG, 3) as Branch, 
            isnull(SUM(case when Days_Diff between '0' and '3'  then OUT_NET end),0)  as '0 - 3 days',
            isnull(SUM(case when Days_Diff between '4' and '10' then OUT_NET end),0)  as '4 - 10 days',
            isnull(SUM(case when Days_Diff between '11' and '15' then OUT_NET end),0)  as '11 - 15 days',
            isnull(SUM(case when Days_Diff >= '16'  then OUT_NET end),0)  as '16+ days'
                
            from
            (select AUDTORG,INVNUMBER,INVDATE,
            CUSTOMER,TERMS,MAINCUSTYPE,
            datediff([dd] , CONVERT (DATETIME , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1 as Days_Diff,
            OUT_NET from [ARCOUT].dbo.[CUST_OUT]
            where TERMS='Cash') as TblCredit
            group by  TblCredit.AUDTORG
            order by TblCredit.AUDTORG  
                            """, fn.conn)

    # # --------------------- Creating fig-----------------------------------------

    # Data
    r = lib.np.arange(0, 31, 1)
    # print(r)

    # # From raw value to percentage
    totals = [i + j + k + l
              for i, j, k, l in zip(branch_cash_drop_df['0 - 3 days'],
                                          branch_cash_drop_df['4 - 10 days'],
                                          branch_cash_drop_df['11 - 15 days'],
                                          branch_cash_drop_df['16+ days'])]

    all_zero_three = [i / j * 100 for i, j in zip(branch_cash_drop_df['0 - 3 days'], totals)]
    all_four_ten = [i / j * 100 for i, j in zip(branch_cash_drop_df['4 - 10 days'], totals)]
    all_eleven_fifteen = [i / j * 100 for i, j in zip(branch_cash_drop_df['11 - 15 days'], totals)]
    all_sixteen_therty = [i / j * 100 for i, j in zip(branch_cash_drop_df['16+ days'], totals)]

    # #
    # plot
    barWidth = 0.85
    names = branch_cash_drop_df['Branch']
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

    # lib.plt.figure(figsize=(12.81, 9))

    series_labels = ['0 - 3 days', '4 - 10 days', '11 - 15 days', '16+ days']

    data = [
        all_zero_three,
        all_four_ten,
        all_eleven_fifteen,
        all_sixteen_therty
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

    #lib.plt.xlabel("Branch Name", fontweight='bold', fontsize=12)
    lib.plt.ylabel("Percentage %", fontweight='bold', fontsize=12)
    lib.plt.title('12. Branch Wise Cash Drop', fontsize=16, fontweight='bold', color='#3e0a75')
    lib.plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.085),
                   fancybox=True, shadow=True, ncol=7)
    # lib.plt.show()
    # lib.plt.close()
    lib.plt.savefig('./Images/12.branch_wise_cash_drop_aging.png')
    print('12.	Branch wise Cash Drop Aging')
