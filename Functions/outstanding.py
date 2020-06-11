from Functions import all_library as lib
import Functions.all_function as fn


def totalOutstanding():
    outstanding_df = lib.pd.read_sql_query(""" select
                    SUM(CASE WHEN TERMS='CASH' THEN OUT_NET END) AS TotalOutStandingOnCash,
                    SUM(CASE WHEN TERMS not like '%CASH%' THEN OUT_NET END) AS TotalOutStandingOnCredit
                    from  [ARCOUT].dbo.[CUST_OUT]
                    where [INVDATE] <= convert(varchar(8),DATEADD(D,0,GETDATE()),112)
                                           
                     """, fn.conn)

    cash = int(outstanding_df['TotalOutStandingOnCash'])
    credit = int(outstanding_df['TotalOutStandingOnCredit'])

    data = [cash, credit]
    total = cash + credit
    total = 'Total \n' + fn.numberInThousands(total)

    colors = ['#f9ff00', '#ff8600']

    legend_element = [lib.Patch(facecolor='#f9ff00', label='Cash'),
                      lib.Patch(facecolor='#ff8600', label='Credit')]

    data_label = [fn.numberInThousands(cash), fn.numberInThousands(credit)]

    fig1, ax = lib.plt.subplots()
    # Add this next line to show data
    wedges, labels, autopct = ax.pie(data, labels=data_label, colors=colors, autopct='%.1f%%', textprops={
        'color':"Black"},startangle=90,pctdistance=.7)

    lib.plt.setp(autopct, fontsize=14, color='blue', fontweight='bold')
    lib.plt.setp(labels, fontsize=14, fontweight='bold')

    # To make a Donate chart uncomment next 4 lines ------------
    ax.text(0, -.1, total, ha='center', fontsize=14, fontweight='bold')
    centre_circle = lib.plt.Circle((0, 0), 0.50, fc='white')
    fig = lib.plt.gcf()
    fig.gca().add_artist(centre_circle)
    lib.plt.title('1. Total Outstanding', fontsize=16, fontweight='bold', color='#3e0a75')
    ax.axis('equal')
    lib.plt.legend(handles=legend_element, loc='lower left', fontsize=11)
    lib.plt.tight_layout()
    lib.plt.savefig('./Images/1.total_outstanding.png')
    print('1.Total Outstanding Generated')
