import re
import csv
f = open('Artworks.csv', 'r')

directory = open("Artworks.csv", "r")
booze = open("edit1.csv", "w")

# #this pattern pulls out all the distillers/distilleries and brewers/breweries
# patternDistill = re.compile('(.*)(D|d)istill(.*)')
# patternBrew1 = re.compile('(.*)(B|b)rewer(.*)')
# patternBrew2 = re.compile('(.*)(B|b)rewing(.*)')
# #this regex splits the text before and after numerals -- creates name/address split
# pattern1 = re.compile('([a-z]+.*?)([0-9]+.*)', re.IGNORECASE)
# pattern2 = re.compile('[^A-Za-z0-9]+', re.IGNORECASE)


#results = regex.findall(directory)

with open('edit2.csv', mode='w') as new_file:
	csv_writer = csv.writer(new_file, delimiter=',', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
		
	csv_writer.writerow(line)

	
	# for line in open("prohibition.txt"):
	# 	#search for all instances of the word "distill"
	# 		r1 = patternDistill.search(line)
	# 		if r1 != None:
	# 			#remove weird 44s
	# 			newline = line.replace('44', '')
	# 			newline = newline.replace('av', 'ave')
	# 			newline = newline.replace(' h ', '')
	# 			newline = newline.replace(' k ', '')
	# 			newline = newline.replace(' b ', '')
	# 			newline = newline.replace(' , ', '')
	# 			#split the lines into cells using the regex pattern defined above
	# 			splitLine = pattern1.split(newline)
	# 			del splitLine[0]
	# 			project_writer.writerow(splitLine)
	# 		#search directory for all instances of word "brew"	
	# 		r2 = patternBrew.search(line)
	# 		if r2 != None:
	# 			newline = line.replace('44', '')
	# 			newline = newline.replace('av', 'ave')
	# 			newline = newline.replace(' h ', '')
	# 			newline = newline.replace(' k ', '')
	# 			newline = newline.replace(' b ', '')
	# 			newline = newline.replace(' , ', '')
	# 			#split the lines into cells using the regex pattern defined above
	# 			splitLine = pattern1.split(newline)
	# 			del splitLine[0]
	# 			#write the split up lines to the csv file
	# 			project_writer.writerow(splitLine)
	# 		r3 = patternBrew2.search(line)
	# 		if r2 != None:
	# 			newline = line.replace('44', '')
	# 			newline = newline.replace('av', 'ave')
	# 			newline = newline.replace(' h ', '')
	# 			newline = newline.replace(' k ', '')
	# 			newline = newline.replace(' b ', '')
	# 			newline = newline.replace(' , ', '')
	# 			#split the lines into cells using the regex pattern defined above
	# 			splitLine = pattern1.split(newline)
	# 			del splitLine[0]
	# 			#write the split up lines to the csv file
		csv_writer.writerow(line)


#Stuff that doesn't work for removing edge cases:

 #for line in input:
 	#if line.strip("\n") != "brewster":
		#output.write(line)

#patternBrew = re.compile('(.*)(B|b)rewer','(.*)(B|b)rewing')

#patternBrew = re.compile('Hebrew|Brewster|Brewi|Brewington|((.*)(B|b)rew(.*))')
#this thing above might actually work - i don't get any errors - but for some reason my csv is now blank even if i don't put this change in

