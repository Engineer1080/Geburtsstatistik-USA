import matplotlib.pyplot as plt

xs = []
ys = []

name = input("Bitte geben Sie einen beliebigen Vornamen an. ")
gender = input("Bitte geben Sie das Geschlecht des Namens an. (M oder F) ")
gender = gender.upper()
state = input("Bitte geben Sie den US-Bundesstaat an. (z.B. CA für Kalifornien) ")
state = state.upper()
startyear = int(input("Bitte geben Sie das Anfangsjahr ein. "))
endyear = int(input("Bitte geben Sie das Endjahr ein. "))
namecount = 0
if gender == "M":
    gendername = " Männer"
else:
    gendername = " Frauen"

with open("data/data/names.csv", "r") as file:
    counter = 0
    for line in file:
        counter = counter + 1
        line_splitted =  line.strip().split(",")
        if line_splitted[1] == name and line_splitted[3] == gender and line_splitted[4] == state and int(line_splitted[2]) >= startyear and int(line_splitted[2]) <= endyear:
            xs.append(int(line_splitted[2]))
            ys.append(int(line_splitted[5]))
            namecount = namecount + int(line_splitted[5])

#print(xs)
#print(ys)
print()
print("Es wurden zwischen dem Jahr " + str(startyear) +" und " + str(endyear) + " " + str(namecount) + gendername + " mit dem Namen " + name + " in " + state +" geboren.")
plt.plot(xs,ys)
plt.show()
