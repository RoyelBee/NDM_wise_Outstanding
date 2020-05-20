import pandas as pd
import numpy as np

import Functions.all_library as lib
import Functions.all_function as fn

valuess = pd.read_csv('E:/NDM_wise_Outstanding/Functions/branchIwise_outstanding.csv', index_col=False)
print(valuess.columns)

branch = valuess['Branch']
zero_three = valuess['0 - 3 days']
four_ten = valuess['4 - 10 days']
eleven_fifteen = valuess['11 - 15 days']
sixteen_therty = valuess['16 - 30 days']
thrtyone_ninety = valuess['31 - 90 days']
ninetyone_twohundredone = valuess['91 - 201 days']
twohundredtwo_more = valuess['202+ days']

# # --------------------- Creating fig-----------------------------------------

# Data
r = np.arange(0, 31, 1)
print(r)

# # From raw value to percentage
totals = [i + j + k + l + m + n + o
          for i, j, k, l, m, n, o in zip(valuess['0 - 3 days'],
                                         valuess['4 - 10 days'],
                                         valuess['11 - 15 days'],
                                         valuess['16 - 30 days'],
                                         valuess['31 - 90 days'],
                                         valuess['91 - 201 days'],
                                         valuess['202+ days'])]

all_zero_three = [i / j * 100 for i, j in zip(valuess['0 - 3 days'], totals)]
all_four_ten = [i / j * 100 for i, j in zip(valuess['4 - 10 days'], totals)]
all_eleven_fifteen = [i / j * 100 for i, j in zip(valuess['11 - 15 days'], totals)]
all_sixteen_therty = [i / j * 100 for i, j in zip(valuess['16 - 30 days'], totals)]
all_thrtyone_ninety = [i / j * 100 for i, j in zip(valuess['31 - 90 days'], totals)]
all_ninetyone_twohundredone = [i / j * 100 for i, j in zip(valuess['91 - 201 days'], totals)]
all_twohundredtwo_more = [i / j * 100 for i, j in zip(valuess['202+ days'], totals)]

# #
# plot
barWidth = 0.85
names = valuess['Branch']
fig, ax = lib.plt.subplots(figsize=(12.81, 9))
print(names)
#labels = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
labels=names.tolist()
def plot_stacked_bar(data, series_labels, category_labels=None,
                     show_values=False, value_format="{}", y_label=None,
                     colors=None, grid=False, reverse=False):
    """Plots a stacked bar chart with the data and labels provided.

    Keyword arguments:
    data            -- 2-dimensional numpy array or nested list
                       containing data for each series in rows
    series_labels   -- list of series labels (these appear in
                       the legend)
    category_labels -- list of category labels (these appear
                       on the x-axis)
    show_values     -- If True then numeric value labels will
                       be shown on each bar
    value_format    -- Format string for numeric value labels
                       (default is "{}")
    y_label         -- Label for y-axis (str)
    colors          -- List of color labels
    grid            -- If True display grid
    reverse         -- If True reverse the order that the
                       series are displayed (left-to-right
                       or right-to-left)
    """

    ny = len(data[0])
    ind = list(range(ny))

    axes = []
    cum_size = np.zeros(ny)

    data = np.array(data)

    if reverse:
        data = np.flip(data, axis=1)
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
                lib.plt.text(bar.get_x() + w/2, bar.get_y() + h/2,
                         value_format.format(h), ha="center",
                         va="center", rotation=90)


lib.plt.figure(figsize=(12.81, 9))

series_labels = ['0 - 3 days', '4 - 10 days', '11 - 15 days', '16 - 30 days', '31 - 90 days', '91 - 201 days', '202+ days']

data = [
    all_zero_three,
    all_four_ten,
    all_eleven_fifteen,
    all_sixteen_therty,
    all_thrtyone_ninety,
    all_ninetyone_twohundredone,
    all_twohundredtwo_more
]

#category_labels = ['Cat A', 'Cat B', 'Cat C', 'Cat D']

plot_stacked_bar(
    data,
    series_labels,
    category_labels=labels,
    show_values=True,
    value_format='{:.0f}% ',
    colors=['#31c377','#f4b300','red','#96ff00','#0089ff','#e500ff','#00ffd8']
)

lib.plt.xlabel("Branch Name", fontweight='bold', fontsize=12)
lib.plt.ylabel("Percentage %", fontweight='bold', fontsize=12)
lib.plt.title('Branch Wise Matured Credit', fontweight='bold', fontsize=12)
lib.plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.085),
          fancybox=True, shadow=True, ncol=7)
print(' ')
lib.plt.show()
#plt.close()
#lib.plt.savefig('E:/NDM_wise_Outstanding/Images/matured_credit_test.png')
print('done')