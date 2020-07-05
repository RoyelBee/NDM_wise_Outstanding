import matplotlib.pyplot as plt
import pandas as pd
import pyodbc as db
from matplotlib.patches import Patch

def convert(number):
    number = number / 1000
    number = int(number)
    number = format(number, ',')
    number = number + 'K'
    return number

connection = db.connect('DRIVER={SQL Server};'
                        'SERVER=137.116.139.217;'
                        'DATABASE=ARCHIVESKF;'
                        'UID=sa;PWD=erp@123')

cursor = connection.cursor()

outstanding_df = pd.read_sql_query(""" select
                SUM(CASE WHEN TERMS='CASH' THEN OUT_NET END) AS TotalOutStandingOnCash,
                SUM(CASE WHEN TERMS not like '%CASH%' THEN OUT_NET END) AS TotalOutStandingOnCredit

                from  [ARCOUT].dbo.[CUST_OUT]
                where AUDTORG like 'BOGSKF' AND [INVDATE] <= convert(varchar(8),DATEADD(D,0,GETDATE()),112)
                                        """, connection)

cash = int(outstanding_df['TotalOutStandingOnCash'])
credit = int(outstanding_df['TotalOutStandingOnCredit'])

data = [cash, credit]
total = cash + credit
total = 'Total \n' + convert(total)

colors = ['green', 'blue']

legend_element = [Patch(facecolor='green', label='Cash'),
                  Patch(facecolor='blue', label='Credit')]

# -------------------new code--------------------------

cash_label = convert(cash)
credit_label = convert(credit)

DataLabel = [cash_label, credit_label]
# -----------------------------------------------------

fig1, ax = plt.subplots()
wedges, labels, autopct = ax.pie(data, colors=colors, labels=DataLabel, autopct='%.1f%%', startangle=90,
                                 pctdistance=.7)
plt.setp(autopct, fontsize=14, color='black', fontweight='bold')
plt.setp(labels, fontsize=14, fontweight='bold')
ax.text(0, -.1, total, ha='center', fontsize=14, fontweight='bold', backgroundcolor='#00daff')

centre_circle = plt.Circle((0, 0), 0.50, fc='white')

fig = plt.gcf()

fig.gca().add_artist(centre_circle)
# Equal aspect ratio ensures that pie is drawn as a circle
plt.title('Outstanding', fontsize=16, fontweight='bold', color='#3e0a75')

ax.axis('equal')
plt.legend(handles=legend_element, loc='lower left',
           fontsize=11)
plt.tight_layout()
plt.show()