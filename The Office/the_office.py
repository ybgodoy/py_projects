import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


data = pd.read_csv('./the_office_series.csv')


# Adding a column with colors according to the scaled ratings
color_conditions = [
    (data['scaled_ratings'] < 0.25),
    (np.logical_and(data['scaled_ratings'] >= 0.25, (data['scaled_ratings'] < 0.50))),
    (np.logical_and(data['scaled_ratings'] >= 0.50, (data['scaled_ratings'] < 0.75))),
    (data['scaled_ratings'] >= 0.75)
]

colors = ['red', 'orange', 'lightgreen', 'darkgreen']

data['colors'] = list(np.select(color_conditions, colors))


# Creating separate dataframes, for different plotting parameters
guest_column = data['GuestStars'].apply(lambda x: False if pd.isnull(x) else True) 

guests = data[guest_column]
no_guests = data[~guest_column]


# Plots
plt.scatter(guests['episode_number'], guests['viewership_mil'], c = guests['colors'], marker = '*', s=250)
plt.scatter(no_guests['episode_number'], no_guests['viewership_mil'], c = no_guests['colors'], s=25)
plt.title("Popularity, Quality, and Guest Appearances on the Office")
plt.xlabel('Episode Number')
plt.ylabel('Viewership (Millions)')
plt.text(90, 21.2, 'Cloris Leachman, Jack Black,\n Jessica Alba')
plt.show()
