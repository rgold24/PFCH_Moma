import csv

with open('Artworks.csv', 'r') as csv_file:
	csv_reader = csv.reader(csv_file)

	print(csv_reader)

	for line in csv_reader:
		print(line)

		