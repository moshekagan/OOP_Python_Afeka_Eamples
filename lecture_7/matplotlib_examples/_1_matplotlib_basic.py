"""
MatPlotLib Basic

Docs:
https://matplotlib.org/3.5.3/api/_as_gen/matplotlib.pyplot.html
"""

import matplotlib.pyplot as plt
import numpy as np

# Crate Basic graph
x = [0, 1, 2, 3, 4]
y = [0, 2, 4, 6, 8]

plt.plot(x, y)

# Add labels and title
plt.title("My First Graph!", fontdict={"fontname": "Comic Sans MS", "fontsize": 20})
plt.xlabel("X Axis!")
plt.ylabel("Y AXis!")

# Change ticks
plt.xticks([0, 1, 2, 3, 4])
plt.yticks([0, 2, 4, 6, 8, 10])

# Change color, label, line width, marker, line style
plt.plot(x, y,
         label="2x",
         color="green",
         linewidth=3,
         marker=".", markersize=10, markeredgecolor="black",
         linestyle="--")

# Add legend
plt.legend()

# Add grid
plt.grid()

# Show graph
plt.show()


