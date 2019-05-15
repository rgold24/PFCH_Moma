import csv


with open('Artworks.csv', r)
f = open('Artworks.csv')

csv_f = csv.reader(f)

gender = []


for row in csv_f:
	gender.append(row[1][4][7])

print (gender)



f.close()