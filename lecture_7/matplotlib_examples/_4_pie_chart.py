"""
Bar Chart
"""

import matplotlib.pyplot as plt
import numpy as np

labels = ["A", "B", "C"]
values = [1, 4, 2]

# create graph
plt.pie(values, labels=labels)

plt.legend(title="My Values:")


# Show graph
plt.show()


