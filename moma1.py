import csv 
from csv import reader 



opened_file = open('artworks.csv')
read_file = reader(opened_file)
moma = list(read_file)
# moma = moma[1:]

#not using this right now
#for later, to use nationalities

nationalities = ['(American)', '(Spanish)', '(French)', '(Dutch']

for row in moma:
    nationality = row[4]
    nationality = nationality.replace('(','')
    nationality = nationality.replace('(','')
    row[4]=nationality 

    gender = row[7]
    gender = gender.replace("(","")
    gender = gender.replace(")","")
    row[7] = gender

artist_freq = {}

for row in moma:
    artist = row[1]
    if artist not in artist_freq:
        artist_freq[artist] = 1
    else:
        artist_freq[artist] += 1

#you can query to find out how many pieces by any particular artist        
def a_summary(artist):
    num_artworks = artist_freq[artist]
    artistsumm = "There are {num} artworks by {name} in the data set"
    output_artist = artistsumm.format(name=artist, num=num_artworks)
    print(output_artist)

a_summary("Louise Bourgeois")
a_summary("Pablo Picasso")

for row in moma:
    gender = row[7]
    gender = gender.title()
    
    if row[7] =="Male Male":
        row[7] = 'Two Men'   

    if not gender:
        gender = "Gender Unknown/Other"
    row[7] = gender

 # to use if dealing with nationality 
  # # fix the capitalization and missing
  #   # values for the nationality column
  #   nationality = row[4]
  #   nationality = nationality.title()
  #   if not nationality:
  #       nationality = "Nationality Unknown"
  #   row[4] = nationality




gender_freq = {}

for row in moma:
    gender = row[7]
    if gender not in gender_freq:
        gender_freq[gender] = 1
    else:
        gender_freq[gender] += 1

#g = gender
for gender, num in gender_freq.items():
    template = "There are {n:,} artworks by {g} artists"
    print(template.format(g=gender, n=num))

#attempt to create summarize gender
# def gender_summary(gender):
#     num_gender = gender_freq[artist]
#     template = "There are {num} artworks by {name} in the data set"
#     output = template.format(name=gender, num=num_artworks)
#     print(output)

# artist_summary("Male, Male")



# # count element ('a', 'b')
# count = gender.count(('male, male'))

# print count
# print("The count of ('male, male') is:", (count.row[7])

# for gender, count in gender_freq.items():
#     output = "I have {g} {n}s".format(n=count, g=gender)
#     print(output)

  
  #KEEP THIS LINE-------------------   

# for gender, num in gender_freq.items():
#     template = "There are {n:,} artworks by {g} artists"
#     print(template.format(g=gender, n=num))
  

    











    # print(template.format(g=gender, n=num))
#put into regex



# for row in moma
#     birth_date = row[6]
#     birth_date = birth_date.replace("(", "")
#     birth_date = birth_date.replace(")", "")


# def clean_and_convert(row[5]):
#     # check that we don't have an empty string
#     if date != "":
#         # move the rest of the function inside
#         # the if statement
#         date = date.replace("(", "")
#         date = date.replace(")", "")
#         date = int(date)
#     return date

# clean_and_convert("")



# def clean_and_convert(date):
#     if date != "" or '0' or '1932 0':
#         date = date.replace("(", "")
#         date = date.replace(")", "")
#         date = int(date)
#     return date

# for row in moma:
#     birth_date=row[5]
#     death_date=row[6]

#     birth_date = clean_and_convert(birth_date)
#     death_date = clean_and_convert(death_date)

# clean_and_convert("")

# # def clean_and_convert(date):
# #     # check that we don't have an empty string
# #     if date != "":
# #         # move the rest of the function inside
# #         # the if statement
# #         date = date.replace("(", "")
# #         date = date.replace(")", "")
# #         date = int(date)
# #     return date

# # clean_and_convert("")


# # bad_chars = ["(",")","c","C",".","s","'", " "]
# # def strip_characters(string):
# #     for char in bad_chars:
# #         string = string.replace(char,"")
# #     return string

# # stripped_test_data = []
# # for d in moma:
# #     date = strip_characters(d)
# #     stripped_test_data.append(date)