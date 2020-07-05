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
                    when Days_Diff >=16  THEN '16+ days'
                    end  as AgingDays,
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
                    where TERMS='Cash') as TblCredit
                    group by
                    case
                    when Days_Diff between 0 and 3  THEN '0 - 3 days'
                    when Days_Diff between 4 and 10  THEN '4 - 10 days'
                    when Days_Diff between 11 and 15  THEN '11 - 15 days'
                    when Days_Diff >=16  THEN '16+ days'
                    end
                    ,CASE
                    when TblCredit.Days_Diff between '0' and '3'  THEN 1
                    when TblCredit.Days_Diff between '4' and '10'  THEN 2
                    when TblCredit.Days_Diff between '11' and '15'  THEN 3
                    ELSE  4
                    end ) as T1
                    group by T1.AgingDays, SERIAL
                    order by SERIAL
                                          """, fn.conn)

    serial = [0, 1, 2, 3]
    all = [i for i in aging_mature_df['Amount']]
    total = sum(all)
    Amount = [i * 100 / total for i, j, in zip(aging_mature_df['Amount'], all)]

    # plot
    barWidth = 0.80
    names = ('0 to 3 Days', '4 to 10 Days', '11 to 15 Days', '16+ Days')
    fig, ax = lib.plt.subplots(figsize=(12.8, 4.8))
    # Create green Bars
    bar1 = lib.plt.bar(serial, all, color='#31c377', label='Matured', edgecolor='white', width=barWidth)

    # Create orange Bars
    for bar in bar1:
        height = bar.get_height()
        ax.text(bar.get_x() +.25, height, str(fn.numberInComma(height)) + 'K',
                ha='center', va='bottom', fontweight='bold')

    for bar, Amount in zip(bar1, Amount):
        height = bar.get_height()
        ax.text(bar.get_x() +.5, height, '('+str("%.2f" % round(Amount, 2)) + '%'+')',
                ha='center', va='bottom',color='blue', fontweight='bold')

    # Custom x axis
    lib.plt.xticks(serial, names)
    # lib.plt.yticks(lib.np.arange(0, 101, 10))
    # lib.plt.xlabel('Aging Days', color='black', fontsize=14, fontweight='bold')
    lib.plt.ylabel('Amount & Percentage %', color='black', fontsize=14, fontweight='bold')
    lib.plt.title('10. Total Cash Drop', fontsize=16, fontweight='bold', color='#3e0a75')
    lib.plt.tight_layout()
    # lib.plt.show()
    print('10. Total Cash Drop Aging')
    return lib.plt.savefig('./Images/10.cashdrop_aging.png')
