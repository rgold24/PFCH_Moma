import io
import requests
import pandas as pd

artists = 'https://media.githubusercontent.com/media/MuseumofModernArt/collection/master/Artists.csv'
artworks = 'https://media.githubusercontent.com/media/MuseumofModernArt/collection/master/Artworks.csv'


artists_r = requests.get(artists).content
artists_df = pd.read_csv(io.StringIO(artists_r.decode('utf-8')))
print(artists_df.describe())
print(artists_df.head())

artworks_r = requests.get(artworks).content
artworks_df = pd.read_csv(io.StringIO(artworks_r.decode('utf-8')))
print(artworks_df.describe())
print(artworks_df.head())

print(artists_df.columns)

# How many rows are in the table?
print(len(artists_df))

# How many unique ConstituentID/rows are there in artists?
len(artists_df.ConstituentID.unique())

print(artworks_df.columns)
print(len(artworks_df))

artworks_df['Gender'].value_counts()

artworks_df['Nationality'].value_counts()

#12
artworks_df['ConstituentID'].value_counts()

artworks_df['Nationality'] = artworks_df['Nationality'].str.replace(r'Nationality Unknown', 'Unknown')
artworks_df['Nationality'] = artworks_df['Nationality'].str.replace(r'Nationality unknown', 'Unknown')
artworks_df['Nationality'] = artworks_df['Nationality'].str.replace(r'nationality unknown', 'Unknown')
artworks_df['Nationality'] = artworks_df['Nationality'].str.replace(r'New Zealander', 'New_Zealander')
artworks_df['Nationality'] = artworks_df['Nationality'].str.replace(r'South African', 'South_African')
artworks_df['Nationality'] = artworks_df['Nationality'].str.replace(r'Saudi Arabian', 'Saudi_Arabian')
artworks_df['Nationality'] = artworks_df['Nationality'].str.replace(r'Puerto Rican', 'Puerto_Rican')
artworks_df['Nationality'] = artworks_df['Nationality'].str.replace(r'Canadian Inuit', 'Canadian_Inuit')
artworks_df['Nationality'] = artworks_df['Nationality'].str.replace(r'Native American', 'Native_American')
artworks_df['Nationality'] = artworks_df['Nationality'].str.replace(r'Costa Rican', 'Costa_Rican')


#15 15 15 15
artworks_df['Gender'] = artworks_df['Gender'].str.replace(r'[\(\)]', '')

#22
Art1 = (artworks_df.drop('Gender', axis=1).join(artworks_df.Gender.str.split(' ', expand=True).stack() \
                                              .reset_index(drop=True, level=1).rename('Gender')))
type(Art1)

#23
len(Art1)

#25
Art2 = (artworks_df.drop('Nationality', axis=1).join(artworks_df.Nationality.str.split(' ', expand=True).stack() \
                                                   .reset_index(drop=True, level=1).rename('Nationality')))
print(type(Art2))
print(len(Art2))

#26
Art3 = (artworks_df.drop('ConstituentID', axis=1).join(artworks_df.ConstituentID.str.split(',', expand=True) \
                                                       .stack().reset_index(drop=True, level=1).rename('ConstituentID')))
print(type(Art3))
print(len(Art3))

#27
nation_list = artworks_df['Nationality'].value_counts()
nation_index = nation_list.index

print(*nation_index)

#32
Art3['Gender'] = Art1['Gender']
Art3.columns

#33
Art3['Gender'].value_counts()

#34
Art3['Nationality'] = Art2['Nationality']

#35
Art3['Nationality'].value_counts()

#36
artworks_df['Artist'].value_counts()

#38
artworks_df['ArtistBio'].value_counts()

#39 
artworks_df['Artist'] = artworks_df['Artist'].str.replace(r' ', '')
artworks_df['Artist'].value_counts()

#40
Art4 = (artworks_df.drop('Artist', axis=1).join(artworks_df.Artist.str.split(',', expand=True) \
                                                       .stack().reset_index(drop=True, level=1).rename('Artist')))
print(type(Art4))
print(len(Art4))

#41
Art4['Artist'].value_counts()

#43
Art3['Gender'] = Art3['Gender'].str.replace(r'male', 'Male')

#44
Art3['Gender'].value_counts()

#47
Art3['Gender'] = Art3['Gender'].str.replace(r'FeMale', 'Female', regex=True)
Art3['Gender'] = Art3['Gender'].str.replace(r'feMale', 'Female', regex=True)

#48
Art3['Gender'].value_counts()

#49
Art3 = Art3.rename(index=str, columns={"BeginDate": "Born", "EndDate": "Death"})
Art3.columns

#50
Art3.to_csv('MoMA_artworks.csv')








