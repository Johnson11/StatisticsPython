import matplotlib.pyplot as plt
import numpy as np

#make a histogramm (bar chart with numbers as categories)

nrBins = 11
values = [72,79,81,80,63,62,89,99,50,78,87,97,55,69,97,\
	87,88,99,76,78,65,77,88,90,81]
bins = np.linspace(min(values),max(values),nrBins)

plt.title("Test Results (n=25)")
plt.hist(values,bins)
plt.xlabel("Points")
plt.ylabel("Absolute frequency")

plt.show()

