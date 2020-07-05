import Functions.all_library as lib
import Functions.all_function as fn

def total_non_matured_credit_aging():
    data = lib.pd.read_sql_query("""
            SELECT  
            isnull(SUM(case when TblCredit.Days_Diff between '-3' and '0'  THEN OUT_NET end), 0)/1000  as '0 - 3 days',
            isnull(sum(case when TblCredit.Days_Diff between '-10' and '-4'  THEN OUT_NET end), 0)/1000 as  '4 - 10 days', 
            isnull(sum( case when TblCredit.Days_Diff between '-15' and '-11'  THEN OUT_NET end), 0)/1000 as '11 - 15 days', 
            isnull(sum(case when TblCredit.Days_Diff between '-30' and '-16'  THEN OUT_NET end), 0)/1000 as '16 - 30 days', 
            isnull(sum(case when TblCredit.Days_Diff between '-90' and '-31'  THEN OUT_NET end), 0)/1000 as '31 - 90 days', 
            isnull(sum( case when TblCredit.Days_Diff between '-201' and '-91'  THEN OUT_NET end), 0)/1000 as '90 - 201 days', 
            isnull(sum( case when TblCredit.Days_Diff <= '-202'  THEN OUT_NET end), 0)/1000 as '202+ days'
            from
            (select CUSTNAME, INVNUMBER,INVDATE,
            CUSTOMER,TERMS,MAINCUSTYPE,
            CustomerInformation.CREDIT_LIMIT_DAYS,
            (datediff([dd] , CONVERT (DATETIME , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1-CREDIT_LIMIT_DAYS) as Days_Diff,
            OUT_NET from [ARCOUT].dbo.[CUST_OUT]
            join ARCHIVESKF.dbo.CustomerInformation
            on [CUST_OUT].CUSTOMER = CustomerInformation.IDCUST
            where --[ARCOUT].dbo.[CUST_OUT].AUDTORG like ? and 
            TERMS<>'Cash' and (datediff([dd] , CONVERT (DATETIME , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1-CREDIT_LIMIT_DAYS)<=0
            ) as TblCredit """, fn.conn)

    # data = lib.pd.read_excel('D:/Python Code/NDM_wise_Outstanding/Data/total_non_matured_ageing.xlsx', index_col=False)
    # print(data.columns)

    zero_three = int(data['0 - 3 days'])
    four_ten = int(data['4 - 10 days'])
    eleven_fifteen = int(data['11 - 15 days'])
    sixteen_therty = int(data['16 - 30 days'])
    thrtyone_ninety = int(data['31 - 90 days'])
    ninetyone_twohundredone = int(data['90 - 201 days'])
    twohundredtwo_more = int(data['202+ days'])

    serial = [0, 1, 2, 3, 4, 5, 6]
    data = [zero_three, four_ten, eleven_fifteen, sixteen_therty, thrtyone_ninety, ninetyone_twohundredone,
            twohundredtwo_more]

    # print(data)
    total = sum(data)
    data_point = []
    for i in range(len(data)):
        a = (data[i] * 100 / total)
        # print(a)
        data_point.append(a)

    # print('Data set = ', data_point)
    barWidth = 0.80
    names = ('A- 0 to 3 Days', 'B- 4 to 10 Days', 'C- 11 to 15 Days', 'D- 16 to 30 Days', 'E- 31 to 90 Days',
             'F- 91 to 201 Days', 'G- 202+ Days')
    fig, ax = lib.plt.subplots(figsize=(12.8, 4.8))
    # Create green Bars
    bar1 = lib.plt.bar(serial, data, color='#ffb667', label='Matured', edgecolor='white', width=barWidth)

    # Create orange Bars
    for bar in bar1:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height, str(fn.numberInComma(height))+'K',
                ha='center',
                va='bottom',
                fontweight='bold')

    for bar, percentage in zip(bar1, data_point):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height * .4, str('%.2f' % percentage) + '%', ha='center',
                va='bottom')

    # Custom x axis
    lib.plt.xticks(serial, names)
    # lib.plt.yticks(lib.np.arange(0, 101, 10))
    #lib.plt.xlabel('Aging Days', color='black', fontsize=14, fontweight='bold')
    lib.plt.ylabel('Amount (In Thousands)', color='black', fontsize=14, fontweight='bold')
    lib.plt.title('7. Non-Matured Credit Aging', color='#3e0a75', fontweight='bold', fontsize=16)
    lib.plt.tight_layout()
    # lib.plt.show()
    print('7. Non-Matured Credit Aging Created')
    lib.plt.savefig('./Images/7.non_matured_credit_aging.png')

