#7. Observe os espaços sublinhados e complete o código.
#import numpy as np
#import __________ as mpl
#import __________.______ as plt
#x = np.________(-2 * np.pi, 2 * np.pi, 100)
#y = np.____(x)
#__, __ = plt.subplots()
#ax.____(_, _)


import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)