import Functions.all_library as lib
import Functions.all_function as fn

def ndm_wise_outstanding():
    all_ndm_df = lib.pd.read_sql_query("""
            Select SHORTNAME,
isnull(SUM(case when TblCredit.Days_Diff>0  THEN (OUT_NET) end), 0) as 'Matured',
isnull(SUM(case when TblCredit.Days_Diff<=0  THEN (OUT_NET) end), 0) as 'Non-Matured', 
SUM(OUT_NET) as 'Total'

from
((select CUST_OUT.AUDTORG,INVNUMBER,INVDATE,CUSTOMER,TERMS,MAINCUSTYPE, CustomerInformation.CREDIT_LIMIT_DAYS,
datediff([dd] , CONVERT (DATETIME , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1-CREDIT_LIMIT_DAYS as Days_Diff,
OUT_NET from [ARCOUT].dbo.[CUST_OUT]
join ARCHIVESKF.dbo.CustomerInformation
on [CUST_OUT].CUSTOMER = CustomerInformation.IDCUST
where TERMS<>'Cash' ) as TblCredit
left join 
(select BRANCH, NDMID, SHORTNAME from ARCHIVESKF.dbo.NDM) as NDM
on TblCredit.AUDTORG= NDM.BRANCH
)
group by SHORTNAME
order by SUM(OUT_NET) desc
""", fn.conn)

    all_ndm_matured_credit=all_ndm_df['Matured'].values.tolist()
    all_ndm_non_matured_credit = all_ndm_df['Non-Matured'].values.tolist()

    # # --------------------- Creating fig-----------------------------------------

    # Data
    r = [0, 1, 2, 3, 4]
    data = {'all_matured': all_ndm_matured_credit,
            'all_regular': all_ndm_non_matured_credit}
    df = lib.pd.DataFrame(data)

    # From raw value to percentage
    totals = [i + j for i, j in zip(df['all_matured'], df['all_regular'])]
    all_matured_p = [i / j * 100 for i, j in zip(df['all_matured'], totals)]
    all_regular_p = [i / j * 100 for i, j in zip(df['all_regular'], totals)]

    total = []
    for x in range(len(totals)):
        a = int(totals[x]/1000)
        total.append(a)

    matured = []
    regular = []
    for i in range(len(df['all_matured'])):
        b = int(df['all_matured'][i]/1000)
        matured.append(b)

    for i in range(len(df['all_regular'])):
        b = int(df['all_regular'][i]/1000)
        regular.append(b)

    barWidth = 0.75
    names = all_ndm_df['SHORTNAME']

    fig, ax = lib.plt.subplots(figsize=(12.8, 4.8))
    # bar0 = lib.plt.bar(r, total, width=barWidth, color=None)
    bar1 = lib.plt.bar(r, matured, color='#b35e00', label='Matured', width=barWidth)
    bar2 = lib.plt.bar(r, regular, bottom=matured, color='#ffb667', label='Non-Matured', width=barWidth)

    # # Set Matured Data Point
    matured = all_ndm_matured_credit
    for bar, matured, all_matured in zip(bar1, matured, all_matured_p):
        height = bar.get_height()
        # # This text is for actual matured data label
        ax.text(bar.get_x() + bar.get_width() / 2, height * .6,
                str(fn.numberInThousands(matured)),
                ha='center', va='bottom', fontweight='bold')

        # # This text is for percentage
        ax.text(bar.get_x() + bar.get_width() / 2, height * .1,
                str("%.2f" % all_matured) + '%',
                ha='center', va='bottom', color='white')

    # # Set Non Mature Data Point
    regular = all_ndm_non_matured_credit
    for bar, regular, all_regular in zip(bar2, regular, all_regular_p):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height * .8,
                str(fn.numberInThousands(regular)),
                ha='center', va='bottom', fontweight='bold')

        # # This text is for percentage
        ax.text(bar.get_x() + bar.get_width() / 2, height * .7,
                str("%.2f" % all_regular) + '%',
                ha='center', va='bottom', color='white')

    lib.plt.xticks(r, names)
    max_total = max(totals)/1000

    lib.plt.yticks(lib.np.arange(0, int(max_total) + max_total/10, 10000))
    lib.plt.ylabel("Amount (In Thousands)", fontweight='bold', fontsize=12)
    lib.plt.title('3. NDM wise Credit', fontsize=16, fontweight='bold', color='#3e0a75')
    lib.plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.065),
                   fancybox=True, shadow=True, ncol=4)
    lib.plt.tight_layout()
    print('3. NDM wise Credit Outstanding')
    lib.plt.savefig('./Images/3.ndm_credit_outstanding.png')
    # lib.plt.show()