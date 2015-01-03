
import matplotlib.pyplot as pyplot
#S 38 Aufg 1

gelesen = 86.0
gesamt = 396.0
rest = gesamt - gelesen
 
#make percentages
print "Bis zum Viertel sind es noch: ",(0.25*gesamt)-gelesen," Seiten."
x_list = [gelesen,rest]
label_list = ["Gelesen","Verbleibend"]

pyplot.figure()
pyplot.subplot(211) 
pyplot.axis("equal")
pyplot.pie(
        x_list,
        labels=label_list,
        autopct="%1.1f%%"
        )
pyplot.title("Statistic for Dummies Progress")

#Lesezeit
#150 minuten
# 86 seiten -> 150 minuten
# 1 seite -> 160/86
eineSeite = 150.0/gelesen
print "Fuer eine Seite Brauche Ich: ",eineSeite," Minuten."
print "Fuer alles bis jetzt habe Ich ",(eineSeite*gelesen)/60," Stunden gebraucht."
print "Also werde Ich bis zum Ende noch ",(eineSeite*rest)/60," Stunden brauchen!"
pyplot.subplot(212)
pyplot.bar(1,(eineSeite*gelesen)/60,align="center")
pyplot.bar(2,(eineSeite*rest)/60,align="center")
pyplot.xticks([1,2],["Gelesen","Verbleibend"])
pyplot.ylabel("Stunden")

pyplot.show()
