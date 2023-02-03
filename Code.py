import numpy as np
import matplotlib.pyplot as plt
# y-axis in bold
plt.ylabel('Number', fontweight='normal', color='red', fontsize='10', horizontalalignment='center')
plt.xlabel('Group', fontweight='bold', color='red', fontsize='10', horizontalalignment='center')
# Values of each group
bars1 = [12, 28, 1, 8, 22]
bars2 = [28, 17, 16, 4, 10]
bars3 = [25, 13, 23, 25, 17]
# Heights of bars1 + bars2
bars = np.add(bars1, bars2).tolist()
# The position of the bars on the x-axis
r = [0, 1, 2, 3, 4]
# Names of group and bar width
gene = ['RLK', 'RLP', 'CNL', 'TNL', 'TX']
barWidth = 1
# Create brown bars
plt.bar(r, bars1, color='#7f6d5f', edgecolor='white', width=barWidth)
# Create green bars (middle), on top of the firs ones
plt.bar(r, bars2, bottom=bars1, color='#557f2d', edgecolor='white', width=barWidth)
# Create green bars (top)
plt.bar(r, bars3, bottom=bars, color='#2d7f5e', edgecolor='white', width=barWidth)
# Custom X axis
plt.xticks(r, gene, fontweight='bold')
plt.show()
