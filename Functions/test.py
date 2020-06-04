

# libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import pandas as pd

# Data
r = [0, 1, 2, 3, 4]
raw_data = {'greenBars': [20, 1.5, 7, 10, 5],
            'orangeBars': [5, 15, 5, 10, 15]}
df = pd.DataFrame(raw_data)

# From raw value to percentage
totals = [i + j for i, j in zip(df['greenBars'], df['orangeBars'])]
greenBars = [i / j * 100 for i, j in zip(df['greenBars'], totals)]
orangeBars = [i / j * 100 for i, j in zip(df['orangeBars'], totals)]


# plot
barWidth = 0.85
names = ('A', 'B', 'C', 'D', 'E')
# Create green Bars
plt.bar(r, greenBars, color='#b5ffb9', edgecolor='white', width=barWidth)
# Create orange Bars
plt.bar(r, orangeBars, bottom=greenBars, color='#f9bc86', edgecolor='white', width=barWidth)

# Custom x axis
plt.xticks(r, names)
plt.xlabel("group")

# Show graphic
plt.show()