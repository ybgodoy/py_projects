import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv('./the_office_series.csv')

color_conditions = [
    (data['scaled_ratings'] < 0.25),
    (np.logical_and(data['scaled_ratings'] >= 0.25, (data['scaled_ratings'] < 0.50))),
    (np.logical_and(data['scaled_ratings'] >= 0.50, (data['scaled_ratings'] < 0.75))),
    (data['scaled_ratings'] >= 0.75)
]

colors = ['red', 'orange', 'lightgreen', 'darkgreen']

data['colors'] = list(np.select(color_conditions, colors))

guest_list = []

for lab, row in data.iterrows():
    if(pd.isnull(row['GuestStars'])):
        guest_list.append(False)
    else:
        guest_list.append(True)
        
data['has_guests'] = guest_list

guests = data[data['has_guests']]
no_guests = data[~data['has_guests']]

#print(guests.loc[guests['viewership_mil'].idxmax()])

fig = plt.figure()
plt.scatter(guests['episode_number'], guests['viewership_mil'], c = guests['colors'], marker = '*', s=250)
plt.scatter(no_guests['episode_number'], no_guests['viewership_mil'], c = no_guests['colors'], s=25)
plt.title("Popularity, Quality, and Guest Appearances on the Office")
plt.xlabel('Episode Number')
plt.ylabel('Viewership (Millions)')
plt.text(90, 21.2, 'Cloris Leachman, Jack Black,\n Jessica Alba')
plt.show()
