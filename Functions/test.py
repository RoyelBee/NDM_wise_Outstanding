import pandas as pd
import numpy as np

import Functions.all_library as lib
import Functions.all_function as fn

data = pd.read_csv('E:/NDM_wise_Outstanding/Functions/branchIwise_outstanding.csv', index_col=False)
print(data.columns)

branch = data['Branch']
zero_three = data['0 - 3 days']
four_ten = data['4 - 10 days']
eleven_fifteen = data['11 - 15 days']
sixteen_therty = data['16 - 30 days']
thrtyone_ninety = data['31 - 90 days']
ninetyone_twohundredone = data['91 - 201 days']
twohundredtwo_more = data['202+ days']

# # --------------------- Creating fig-----------------------------------------

# Data
r = np.arange(0, 31, 1)
print(r)

# # From raw value to percentage
totals = [i + j + k + l + m + n + o
          for i, j, k, l, m, n, o in zip(data['0 - 3 days'],
                                         data['4 - 10 days'],
                                         data['11 - 15 days'],
                                         data['16 - 30 days'],
                                         data['31 - 90 days'],
                                         data['91 - 201 days'],
                                         data['202+ days'])]

all_zero_three = [i / j * 100 for i, j in zip(data['0 - 3 days'], totals)]
all_four_ten = [i / j * 100 for i, j in zip(data['4 - 10 days'], totals)]
all_eleven_fifteen = [i / j * 100 for i, j in zip(data['11 - 15 days'], totals)]
all_sixteen_therty = [i / j * 100 for i, j in zip(data['16 - 30 days'], totals)]
all_thrtyone_ninety = [i / j * 100 for i, j in zip(data['31 - 90 days'], totals)]
all_ninetyone_twohundredone = [i / j * 100 for i, j in zip(data['91 - 201 days'], totals)]
all_twohundredtwo_more = [i / j * 100 for i, j in zip(data['202+ days'], totals)]

# #
# plot
barWidth = 0.85
names = data['Branch']
fig, ax = lib.plt.subplots(figsize=(12.81, 9))
# Create green Bars
bar1 = lib.plt.bar(r, all_zero_three, color='#31c377', label='Matured', edgecolor='white', width=barWidth)
# Create orange Bars
bar2 = lib.plt.bar(r, all_four_ten, bottom=all_zero_three, color='#f4b300', label='Non-Matured', edgecolor='white',
                   width=barWidth)

two_bars = np.add(all_zero_three, all_four_ten).tolist()
bar3 = lib.plt.bar(r, all_eleven_fifteen, bottom=two_bars, color='red', label='Non-Matured', edgecolor='white',
                   width=barWidth)

three_bars = np.add(two_bars, all_eleven_fifteen).tolist()
bar4 = lib.plt.bar(r, all_sixteen_therty, bottom=three_bars, color='#96ff00', label='Non-Matured', edgecolor='white',
                   width=barWidth)

four_bars = np.add(three_bars, all_sixteen_therty).tolist()
bar5 = lib.plt.bar(r, all_thrtyone_ninety, bottom=four_bars, color='#0089ff', label='Non-Matured', edgecolor='white',
                   width=barWidth)

five_bars = np.add(four_bars, all_thrtyone_ninety).tolist()
bar6 = lib.plt.bar(r, all_ninetyone_twohundredone, bottom=five_bars, color='#e500ff', label='Non-Matured', edgecolor='white',
                   width=barWidth)

six_bars = np.add(five_bars, all_ninetyone_twohundredone).tolist()
bar6 = lib.plt.bar(r, all_twohundredtwo_more, bottom=six_bars, color='#00ffd8', label='Non-Matured', edgecolor='white',
                   width=barWidth)

for bar, zero_three in zip(bar1, zero_three):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, height * .4, str(int(height)) + '%',
            ha='center', va='bottom', fontweight='bold', rotation=90)

for bar, four_ten in zip(bar2, four_ten):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, height, str(int(height)) + '%',
            ha='center', va='bottom', fontweight='bold', rotation=90)

for bar, eleven_fifteen in zip(bar3, eleven_fifteen):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, height, str(int(height)) + '%',
            ha='center', va='bottom', fontweight='bold', rotation=90)

# Custom x axis
lib.plt.xticks(r, names, rotation=90)
lib.plt.xlabel("NDM Name", fontweight='bold', fontsize=12)
lib.plt.ylabel("Percentage %", fontweight='bold', fontsize=12)
lib.plt.title('NDM wise Credit', fontweight='bold', fontsize=12)
lib.plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.09),
          fancybox=True, shadow=True, ncol=7)
print(' ')
# lib.plt.savefig('./Images/aa.png')
lib.plt.show()
