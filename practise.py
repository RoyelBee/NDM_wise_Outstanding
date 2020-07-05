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


cash = 1000000
credit = 1900000

data = [cash, credit]
total = cash + credit
total = 'Total \n' + convert(total)

colors = ['#e03efa', '#ff4d4d']

legend_element = [Patch(facecolor='green', label='Cash'),
                  Patch(facecolor='blue', label='Credit')]

# -------------------new code--------------------------

cash_label = convert(cash)
credit_label = convert(credit)

DataLabel = [cash_label, credit_label]
# -----------------------------------------------------

fig1, ax = plt.subplots(figsize=(1.7,1.7),facecolor='#0c547c')
wedges, labels, autopct = ax.pie(data,radius=.1, colors=colors, autopct='%.1f%%', startangle=90,
                                 pctdistance=.79)
plt.setp(autopct, fontsize=5, color='black', fontweight='bold')
#plt.setp(labels, fontsize=3, fontweight='bold')
ax.text(0, -.009, total, ha='center', fontsize=5, fontweight='bold', backgroundcolor='#00daff')
#
centre_circle = plt.Circle((0, 0), 0.06, fc='#0c547c')

fig = plt.gcf()

fig.gca().add_artist(centre_circle)
# Equal aspect ratio ensures that pie is drawn as a circle
#plt.title('Outstanding', fontsize=16, fontweight='bold', color='#3e0a75')

ax.axis('equal')
ax.set_facecolor('yellow')
# plt.legend(handles=legend_element, loc='lower left',
#            fontsize=11)
plt.tight_layout()
plt.show()