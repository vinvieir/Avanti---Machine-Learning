#6. Observe os espaços sublinhados e complete o código.
#import __________.pyplot as plt
#import numpy as ___
#fig, axs = plt.subplots(ncols=2, nrows=2, figsize=(5.5, 3.5),
# layout="constrained")
#for ___ in range(2):
# for ___ in range(2):
# axs[row, col].annotate(f'axs[{row}, {col}]', (0.5, 0.5),
# transform=axs[row, col].transAxes,
# ha='center', va='center', ________=18,
# color='darkgrey')
#fig.suptitle('__.subplots()')

import matplotlib.pyplot as plt
import numpy as np

fig, axs = plt.subplots(ncols=2, nrows=2, figsize=(5.5, 3.5),
                        layout="constrained")

for row in range(2):
    for col in range(2):
        axs[row, col].annotate(f'axs[{row}, {col}]', (0.5, 0.5),
                               transform=axs[row, col].transAxes,
                               ha='center', va='center', fontsize=18,
                               color='darkgrey')

fig.suptitle('plt.subplots()')
