import matplotlib.pyplot as plt
import numpy as np
#Balkendiagramme

plt.figure()
plt.title("Befragung zum Thema Rauchverbot")

#Daten in Prozent
Ja = 50
Nein = 25
Enthaltung = 25

data = [Ja,Nein,Enthaltung]
labels = ["Ja","Nein","Enthaltung"]
colors = ["g","r","b"]
#bar needs 1. Bins as numbers, then the values. afte rthat center the strings
barwidth = 0.35
xaxis = np.arange(len(data))
for position in xaxis:
	plt.bar(position,data[position],barwidth,label=labels[position],align="center",\
	color=colors[position])

#now replacing the numbers with the actual strings
plt.xticks(xaxis,labels)

plt.ylabel("Percentage")
plt.xlabel("Answer given")
plt.legend()
plt.show()
