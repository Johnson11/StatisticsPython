
import matplotlib.pyplot as pyplot
#S 38 Aufg 1

gelaendewagen = 150.0
kombi = 125.0
normales = 100.0
gesamt = 375.0
 
#make percentages
p_gelaendewagen = float(gelaendewagen/gesamt)*100
p_kombi = float(kombi/gesamt)*100
p_normales = float(normales/gesamt)*100

x_list = [p_gelaendewagen,p_kombi,p_normales]
label_list = ["Gelaendewagen", "Kombi", "Normales Auto"]
 
pyplot.axis("equal")
pyplot.pie(
        x_list,
        labels=label_list,
        autopct="%1.1f%%"
        )
pyplot.title("Types of Cars (n=375)")
pyplot.show()
