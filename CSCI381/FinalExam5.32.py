"""Exercise 5.32
Making some changes to the original code of RollDie.py, we have to account for the second die in "rolls"
We use sns.barplot(, ,orient="h") to change the orientation of the bar graph."""
import matplotlib.pyplot as plt
import numpy as np
import random
import seaborn as sns


number_of_rolls = int(input('Enter the number of rolls to perform - 360/36,000/36,000,000\n'))

rolls = [random.randrange(1, 7) + random.randrange(1, 7) for i in range(number_of_rolls)]
values, frequencies = np.unique(rolls, return_counts=True)
title = f'Frequencies for {len(rolls):,} Rolls'
sns.set_style("whitegrid")
axes = sns.barplot(frequencies, values, palette='bright', orient="h")
axes.set_title(title)
axes.set(xlabel='Frequency', ylabel='Die Value')
axes.set_xlim(right=max(frequencies) * 1.10)
y_coordinate = 0.3

for bar, frequency in zip(axes.patches, frequencies):
    text_x = 1.01 * frequency
    text_y = y_coordinate
    text = f'{frequency:,}\n{frequency / len(rolls):.3%}'
    axes.text(text_x, text_y, text, fontsize=11, ha='left', va='bottom')
    y_coordinate = y_coordinate + 1
plt.show()

