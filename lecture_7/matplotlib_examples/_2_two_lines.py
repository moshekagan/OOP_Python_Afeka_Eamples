"""
2 lines
Docs:
https://matplotlib.org/3.5.3/api/_as_gen/matplotlib.pyplot.html
"""

import matplotlib.pyplot as plt
import numpy as np

# Add labels and title
plt.title("My First Graph!", fontdict={"fontname": "Comic Sans MS", "fontsize": 20})
plt.xlabel("X Axis!")
plt.ylabel("Y AXis!")

# First line
x = [0, 1, 2, 3, 4]
y = [0, 2, 4, 6, 8]
plt.plot(x, y,
         label="2x",
         color="green",
         linewidth=3,
         marker=".", markersize=10, markeredgecolor="black",
         linestyle="--")

### Line number 2
x2 = np.arange(0, 4.5, 0.5)
print(x2)
plt.plot(x2, x2**2, label="X^2")


# Add legend
plt.legend()

# Show graph
plt.show()


