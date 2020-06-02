import Functions.all_library as lib
import Functions.all_function as fn


# # --- Aging Matured Credit ---------------------------------
def cashdrop_aging():
    aging_mature_df = lib.pd.read_sql_query("""
                         SELECT  AgingDays, sum(Amount)/1000 as Amount FROM (  Select
        case
            when Days_Diff between 0 and 3  THEN '0 - 3 days'
            when Days_Diff between 4 and 10  THEN '4 - 10 days'
            when Days_Diff between 11 and 15  THEN '11 - 15 days'
            when Days_Diff between 16 and 30  THEN '16 - 30 days'
            when Days_Diff between 31 and 90  THEN '31 - 90 days'
            when Days_Diff between 91 and 201  THEN '91 - 201 days'
            else '202+ Days' end  as AgingDays,
        --OUT_NET
        Sum(OUT_NET) as Amount,

        CASE
            when TblCredit.Days_Diff between '0' and '3'  THEN 1
            when TblCredit.Days_Diff between '4' and '10'  THEN 2
            when TblCredit.Days_Diff between '11' and '15'  THEN 3
			when TblCredit.Days_Diff between '16' and '30'  THEN 4
            when TblCredit.Days_Diff between '31' and '90'  THEN 5
            when TblCredit.Days_Diff between '91' and '201'  THEN 6
            ELSE  7
            END AS SERIAL
        from
            (select INVNUMBER,INVDATE,
            CUSTOMER,TERMS,MAINCUSTYPE,
            datediff([dd] , CONVERT (DATETIME , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1 as Days_Diff,
            OUT_NET from [ARCOUT].dbo.[CUST_OUT]
            where TERMS='Cash') as TblCredit
            group by
            case
			when Days_Diff between 0 and 3  THEN '0 - 3 days'
            when Days_Diff between 4 and 10  THEN '4 - 10 days'
            when Days_Diff between 11 and 15  THEN '11 - 15 days'
            when Days_Diff between 16 and 30  THEN '16 - 30 days'
            when Days_Diff between 31 and 90  THEN '31 - 90 days'
            when Days_Diff between 91 and 201  THEN '91 - 201 days'
            else '202+ Days' end
            ,CASE
            when TblCredit.Days_Diff between '0' and '3'  THEN 1
            when TblCredit.Days_Diff between '4' and '10'  THEN 2
            when TblCredit.Days_Diff between '11' and '15'  THEN 3
			when TblCredit.Days_Diff between '16' and '30'  THEN 4
            when TblCredit.Days_Diff between '31' and '90'  THEN 5
            when TblCredit.Days_Diff between '91' and '201'  THEN 6
            ELSE  7
			end ) as T1
            group by T1.AgingDays, SERIAL
        order by SERIAL
                      """, fn.conn)

    serial = [0,1, 2, 3, 4, 5, 6]
    all = [i for i in aging_mature_df['Amount']]
    total = sum(all)
    Amount = [i * 100 / total for i, j, in zip(aging_mature_df['Amount'], all)]

    # plot
    barWidth = 0.80
    names = ('A- 0 to 3 Days', 'B- 4 to 10 Days', 'C- 11 to 15 Days', 'D- 16 to 30 Days', 'E- 31 to 90 Days',
             'F- 91 to 201 Days',
             'G- 202+ Days')
    fig, ax = lib.plt.subplots(figsize=(12.81, 4.8))
    # Create green Bars
    bar1 = lib.plt.bar(serial, Amount, color='#31c377', label='Matured', edgecolor='white', width=barWidth)

    # Create orange Bars
    for bar in bar1:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height * .99, str("%.2f" % round(height, 2))  + '%', ha='center', \
                                                                                                                  va='bottom',
                fontweight='bold')

    # Custom x axis
    lib.plt.xticks(serial, names)
    lib.plt.yticks(lib.np.arange(0, 101, 10))
    lib.plt.xlabel('Aging Days', color='black', fontsize=14, fontweight='bold')
    lib.plt.ylabel('Percentage %', color='black', fontsize=14, fontweight='bold')
    lib.plt.title('Total Cash Drop', color='#3e0a75', fontweight='bold', fontsize=16)
    lib.plt.tight_layout()
    # lib.plt.show()
    print('10. Total Cash Drop Aging')
    return lib.plt.savefig('./Images/10.cashdrop_aging.png')
