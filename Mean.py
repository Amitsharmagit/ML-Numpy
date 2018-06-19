#Mean,Median,Mode and introducing Numpy.
#Mean Vs. Median
#Import numpy library
import numpy as np

incomes = np.random.normal(27000,15000,10000)
np.mean(incomes)

# We can segment the income data into 50 buckets and plot it as a histogram:
#Import matplotlib library for graph.
import matplotlib.pyplot as plt
plt.hist(incomes,50)
plt.show()

# Computing Median
np.median(incomes)

# Adding Bill Gates into the mix. Darn income ineuality.
incomes = np.append(incomes, [1000000000])

#Median Remains almost Same
np.median(incomes)

#Mean Changes distincity
np.mean(incomes)

