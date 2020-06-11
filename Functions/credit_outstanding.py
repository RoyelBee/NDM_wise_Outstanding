from Functions import all_library as lib
import Functions.all_function as fn


def creditOutstanding():
    credit_category_df = lib.pd.read_sql_query(""" Select case when Days_Diff>0 then 'Matured Credit' else 'Regular Credit' End as  'Category',Sum(OUT_NET) as Amount from
                            (select INVNUMBER,INVDATE,
                            CUSTOMER,TERMS,MAINCUSTYPE,
                            CustomerInformation.CREDIT_LIMIT_DAYS,
                            datediff([dd] , CONVERT (DATETIME , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1-CREDIT_LIMIT_DAYS as Days_Diff,
                            OUT_NET from [ARCOUT].dbo.[CUST_OUT]
                            join ARCHIVESKF.dbo.CustomerInformation
                            on [CUST_OUT].CUSTOMER = CustomerInformation.IDCUST
                            where --[ARCOUT].dbo.[CUST_OUT].AUDTORG like ? and 
                            TERMS<>'Cash') as TblCredit
                            group by case when Days_Diff>0 then 'Matured Credit' else 'Regular Credit' end
                                                               
                                                                """, fn.conn)

    matured = int(credit_category_df.Amount.iloc[0])
    not_mature = int(credit_category_df.Amount.iloc[1])

    values = [matured, not_mature]

    colors = ['#ffb667', '#b35e00']

    legend_element = [lib.Patch(facecolor='#ffb667', label='Matured'),
                      lib.Patch(facecolor='#b35e00', label='Not Mature')]

    total_credit = matured + not_mature
    total_credit = 'Total \n' + fn.numberInThousands(total_credit)

    data_label = [fn.numberInThousands(matured), fn.numberInThousands(not_mature)]
    fig1, ax = lib.plt.subplots()
    # Ad this labels=data_label, in next line to add data lebel
    wedges, labels, autopct = ax.pie(values, colors=colors, labels=data_label, autopct='%.1f%%', startangle=90,
                                     pctdistance=.7)
    lib.plt.setp(autopct, fontsize=14, color='black', fontweight='bold')
    lib.plt.setp(labels, fontsize=14, fontweight='bold')

    # Next four lines is for donute chart
    ax.text(0, -.1, total_credit, ha='center', fontsize=14, fontweight='bold')
    centre_circle = lib.plt.Circle((0, 0), 0.50, fc='white')
    fig = lib.plt.gcf()
    fig.gca().add_artist(centre_circle)

    # Equal aspect ratio ensures that pie is drawn as a circle
    lib.plt.title('2. Credit Outstanding', fontsize=16, fontweight='bold', color='#3e0a75')
    ax.axis('equal')
    lib.plt.legend(handles=legend_element, loc='lower left', fontsize=11)
    lib.plt.tight_layout()
    lib.plt.savefig('./Images/2.category_wise_credit.png')
    print('2. Category wise Credit Generated ')
