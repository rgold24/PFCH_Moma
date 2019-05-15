import csv

with open('Artworks.csv', 'r') as csv_file:
	csv_reader = csv.DictReader(csv_file)

# #ea value ordered dictionary 
# 	for line in csv_reader:
# 		print(line['Gender'])



	with open('new_artworks.csv', 'w') as new_file:
		fieldnames = ['\ufeffTitle','Title', 'Artist', 'Nationality', 'BeginDate', 'EndDate', 'Gender', 'Date']
		
		csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)


#inc. headers
		csv_writer.writeheader()

		for line in csv_reader:
			del line['ConstituentID']
			del line['ArtistBio']
			del line['Medium']
			del line['Dimensions']
			del line['CreditLine']
			del line['AccessionNumber']
			del line['Classification']
			del line['Department']
			del line['DateAcquired']
			del line['Cataloged']
			del line['ObjectID']
			del line['URL']
			del line['ThumbnailURL']
			del line['Circumference (cm)']
			del line['Depth (cm)']
			del line['Diameter (cm)']
			del line['Height (cm)']
			del line['Length (cm)']
			del line['Weight (kg)']
			del line['Width (cm)']
			del line['Seat Height (cm)']
			del line['Duration (sec.)']

			# for line in open(Artowrks.csv):
			# 	nationality = row[4]
   #  			nationality = nationality.replace("(","")
   #  			nationality = nationality.replace(")","")
   #  			nationality = nationality.title()
   #  			if not nationality:
   #      			nationality = "Nationality Unknown"
   # 				row[4] = nationality


			csv_writer.writerow(line)





