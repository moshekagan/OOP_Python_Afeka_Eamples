"""
  File  winequality-red.csv
 Attribute information:

   For more information, read [Cortez et al., 2009].

   Input variables (based on physicochemical tests):
   1 - fixed acidity - חומצה קבועה
   2 - volatile acidity - חומצה נדיפה
   3 - citric acid - חומצת לימון
   4 - residual sugar - שאריות סוכר
   5 - chlorides - כלורידים
   6 - free sulfur dioxide - דו תחמוצת גופרית
   7 - total sulfur dioxide - סך דו תחמוצת הגופרית
   8 - density - צפיפות
   9 - pH - רמת חומציות
   10 - sulphates - סולפטים
   11 - alcohol - אלכוהול
   12 - quality (score between 0 and 10) - איכות
"""

# # with list
# import csv
# with open('winequality-red.csv', 'r') as f:
#     wines = list(csv.reader(f, delimiter=','))
# print(wines[:3])
#
# qualities =[float(item[-1]) for item in wines[1:]]
# print(sum(qualities) / len(qualities))
#
# # with numpy
#
# import csv
# with open("winequality-red.csv", 'r') as f:
#     wines = list(csv.reader(f, delimiter=","))
# import numpy as np
# wines = np.array(wines[1:], dtype=float)
# print(wines)
# print(f'The shape of the array is {wines.shape}')

# Alternative NumPy Array Creation Methods
"""
It’s possible to use NumPy to directly read csv or other files into arrays. 

In the below code, we:

Use the genfromtxt function to read in the winequality-red.csv file.
Specify the keyword argument skip_header=1 so that the header row is skipped.
"""

import numpy as np
from matplotlib import pyplot as plt

# Data columns
FIXED_ACIDITY_COL = 0
VOLATILE_ACIDITY_COL = 1
CITRIC_ACID_COL = 2
RESIDUAL_SUGAR_COL = 3
CHLORIDES_COL = 4
FREE_SULFUR_DIOXIDE_COL = 5
TOTAL_SULFUR_DIOXIDE_COL = 6
DENSITY_COL = 7
PH_COL = 8
SULPHATES_COL = 9
ALCOHOL_COL = 10
QUALITY_COL = 11


wines = np.genfromtxt("winequality-red.csv", delimiter=",", skip_header=1)
print(wines)
w0 = wines.sum(axis=0)
print(w0)
print(w0.shape)
print(w0.ndim)
print(type(w0))
w1 = wines.sum(axis=1)
print(w1)
print(w1.shape)
print(type(w1))
print(w1.ndim)
"""
numpy.ndarray.mean — finds the mean of an array.
numpy.ndarray.std — finds the standard deviation of an array.
numpy.ndarray.min — finds the minimum value in an array.
numpy.ndarray.max — finds the maximum value in an array....
"""

# wine.astype(int)

# ph_levels is an array of booleans
ph_levels = wines[:, PH_COL] > 3.5
print(ph_levels)
print()
w = wines[ph_levels]
print(w)
print(w.shape)

# Select only wines where sulphates > 0.7 and alcohol > 7
sulalc = (wines[:, SULPHATES_COL] > 0.7) & (wines[:, ALCOHOL_COL] > 7)
print(wines[sulalc, SULPHATES_COL:])
print()

# select wine having pH greater than mean pH
meanPH = (wines[:, PH_COL] > wines[:, PH_COL].mean())
print(wines[meanPH, PH_COL:])

# adding a new column: diff between quality and quality mean
qmean = round(wines[:, QUALITY_COL].mean(), 2)
qdiff = np.array(wines[:, QUALITY_COL] - qmean)
qdiff = qdiff.reshape(wines.shape[0], 1)
wines = np.hstack([wines, qdiff])
print(wines)

# Is there a correlation between fixed acidity and density
xdata = wines[:100, FIXED_ACIDITY_COL]
ydata = wines[:100, DENSITY_COL]
plt.scatter(xdata, ydata)
plt.title('acidity vs density')
plt.xlabel('acidity')
plt.ylabel('density')
plt.show()
