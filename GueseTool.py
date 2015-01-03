import numpy as np
import matplotlib.pyplot as plt
import math

def mean(X):
	sum = 0.0
	for values in X:
		sum+=values
	return sum/len(X)

def median(X):
	return np.median(X)

def var(X):
	return np.var(X)

def std(X):
	return np.std(X)

def bar(data,labels):
	#bar needs 1. Bins as numbers, then the values. afte rthat center the strings
	barwidth = 0.35
	xaxis = np.arange(len(data))
	for position in xaxis:
		plt.bar(position,data[position],barwidth,label=labels[position],align="center",\
		color=colors[position])

	#now replacing the numbers with the actual strings
	plt.xticks(xaxis,labels)

	plt.ylabel("Percentage")
	plt.xlabel("Labels")
	plt.legend()
	plt.show()

def bar(data,labels,barwidth):
	#bar needs 1. Bins as numbers, then the values. afte rthat center the strings
	xaxis = np.arange(len(data))
	for position in xaxis:
		plt.bar(position,data[position],barwidth,label=labels[position],align="center",\
		color=colors[position])

	#now replacing the numbers with the actual strings
	plt.xticks(xaxis,labels)

	plt.ylabel("Percentage")
	plt.xlabel("Labels")
	plt.legend()
	plt.show()
def bar(data,labels,xlabel,ylabel):
	barwidth=0.35
	xaxis = np.arange(len(data))
	for position in xaxis:
		plt.bar(position,data[position],barwidth,label=labels[position],align="center",\
		color=colors[position])

	#now replacing the numbers with the actual strings
	plt.xticks(xaxis,labels)

	plt.ylabel(ylabel)
	plt.xlabel(xlabel)
	plt.legend()
	plt.show()

def circle(x_list,label_list,title):
	plt.axis("equal")
	plt.pie(
		x_list,
		labels=label_list,
		autopct="%1.1f%%"
		)
	plt.title(title)
	plt.show()

def hist(values,title,xlabel,ylabel):
	nrBins = 10
	values = [72,79,81,80,63,62,89,99,50,78,87,97,55,69,97,\
		87,88,99,76,78,65,77,88,90,81]
	bins = np.linspace(min(values),max(values),nrBins)

	plt.title(title)
	plt.hist(values,bins)
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)

	plt.show()

def hist(values,nrBins):
	values = [72,79,81,80,63,62,89,99,50,78,87,97,55,69,97,\
		87,88,99,76,78,65,77,88,90,81]
	bins = np.linspace(min(values),max(values),nrBins)

	plt.title(title)
	plt.hist(values,bins)
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)

	plt.show()

