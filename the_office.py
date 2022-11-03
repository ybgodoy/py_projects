#!/usr/bin/env python
# coding: utf-8

# ## 1. Welcome!
# <p><img src="https://assets.datacamp.com/production/project_1170/img/office_cast.jpeg" alt="Markdown">.</p>
# <p><strong>The Office!</strong> What started as a British mockumentary series about office culture in 2001 has since spawned ten other variants across the world, including an Israeli version (2010-13), a Hindi version (2019-), and even a French Canadian variant (2006-2007). Of all these iterations (including the original), the American series has been the longest-running, spanning 201 episodes over nine seasons.</p>
# <p>In this notebook, we will take a look at a dataset of The Office episodes, and try to understand how the popularity and quality of the series varied over time. To do so, we will use the following dataset: <code>datasets/office_episodes.csv</code>, which was downloaded from Kaggle <a href="https://www.kaggle.com/nehaprabhavalkar/the-office-dataset">here</a>.</p>
# <p>This dataset contains information on a variety of characteristics of each episode. In detail, these are:
# <br></p>
# <div style="background-color: #efebe4; color: #05192d; text-align:left; vertical-align: middle; padding: 15px 25px 15px 25px; line-height: 1.6;">
#     <div style="font-size:20px"><b>datasets/office_episodes.csv</b></div>
# <ul>
#     <li><b>episode_number:</b> Canonical episode number.</li>
#     <li><b>season:</b> Season in which the episode appeared.</li>
#     <li><b>episode_title:</b> Title of the episode.</li>
#     <li><b>description:</b> Description of the episode.</li>
#     <li><b>ratings:</b> Average IMDB rating.</li>
#     <li><b>votes:</b> Number of votes.</li>
#     <li><b>viewership_mil:</b> Number of US viewers in millions.</li>
#     <li><b>duration:</b> Duration in number of minutes.</li>
#     <li><b>release_date:</b> Airdate.</li>
#     <li><b>guest_stars:</b> Guest stars in the episode (if any).</li>
#     <li><b>director:</b> Director of the episode.</li>
#     <li><b>writers:</b> Writers of the episode.</li>
#     <li><b>has_guests:</b> True/False column for whether the episode contained guest stars.</li>
#     <li><b>scaled_ratings:</b> The ratings scaled from 0 (worst-reviewed) to 1 (best-reviewed).</li>
# </ul>
#     </div>

# In[25]:


# Use this cell to begin your analysis, and add as many as you would like!
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv('datasets/office_episodes.csv')

color_conditions = [
    (data['scaled_ratings'] < 0.25),
    (np.logical_and(data['scaled_ratings'] >= 0.25, (data['scaled_ratings'] < 0.50))),
    (np.logical_and(data['scaled_ratings'] >= 0.50, (data['scaled_ratings'] < 0.75))),
    (data['scaled_ratings'] >= 0.75)
]

colors = ['red', 'orange', 'lightgreen', 'darkgreen']

data['colors'] = list(np.select(color_conditions, colors))

guests = data[data['has_guests']]
no_guests = data[~data['has_guests']]

#print(guests.loc[guests['viewership_mil'].idxmax()])

top_star = 'Jack Black'

fig = plt.figure()
plt.scatter(guests['episode_number'], guests['viewership_mil'], c = guests['colors'], marker = '*', s=250)
plt.scatter(no_guests['episode_number'], no_guests['viewership_mil'], c = no_guests['colors'], s=25)
plt.title("Popularity, Quality, and Guest Appearances on the Office")
plt.xlabel('Episode Number')
plt.ylabel('Viewership (Millions)')
plt.text(90, 21.2, 'Cloris Leachman, Jack Black,\n Jessica Alba')
plt.show()


# In[26]:


get_ipython().run_cell_magic('nose', '', 'import pandas as pd\nimport numpy as np\n\ncolor_data = np.genfromtxt(\'datasets/color_data.csv\', delimiter=\',\')\nbonus_color_data = np.genfromtxt(\'datasets/bonus_color_data.csv\', delimiter=\',\')\nbonus_color_data_2 = np.genfromtxt(\'datasets/bonus_color_data_2.csv\', delimiter=\',\')\nsolution_data = pd.read_csv(\'datasets/solution_data.csv\')\n\nx_axis_data = solution_data[\'x_axis\'].values\ny_axis_data = solution_data[\'y_axis\'].values\nsize_data = solution_data[\'sizes\'].values\n\n\n# Try to retrieve student plot data, if it\'s been specified, otherwise set test values to null\ntry:\n    # Generate x and y axis containers\n    stu_yaxis_cont = []\n    stu_xaxis_cont = []\n    stu_sizes_cont = []\n    stu_colors_cont = []\n\n    # Loop through every axis in student\'s figure and grab x and y data\n    for col in fig.gca().collections:\n        stu_yaxis_cont.append(col._offsets.data[:,1])\n        stu_xaxis_cont.append(col._offsets.data[:,0])\n        stu_sizes_cont.append(np.full((1, len(col._offsets.data[:,0])), col._sizes)[0])\n        stu_colors_cont.append(col._facecolors)\n\n    # Get figure labels\n    title = fig.gca()._axes.get_title()\n    x_label = fig.gca()._axes.get_xlabel()\n    y_label = fig.gca()._axes.get_ylabel()\n\n    # Concatenate lists to compare to test plot\n    stu_yaxis = np.concatenate(stu_yaxis_cont)\n    stu_xaxis = np.concatenate(stu_xaxis_cont)\n    stu_sizes = np.concatenate(stu_sizes_cont)\n    stu_colors = np.concatenate(stu_colors_cont)\nexcept:\n    title = \'null\'\n    x_label = \'null\'\n    y_label = \'null\'\n    stu_yaxis = \'null\'\n    stu_xaxis = \'null\'\n    stu_sizes = [0, 1]\n    stu_colors = [0, 1]\n\n# Tests\ndef test_fig_exists():\n    import matplotlib\n    # Extra function to test for existence of fig to allow custom feedback\n    def test_fig():\n        try:\n            fig\n            return True\n        except:\n            return False\n    assert (test_fig() == True), \\\n    \'Did you correctly initalize a `fig` object using `fig = plt.figure()`?\'\n    assert (type(fig) == matplotlib.figure.Figure), \\\n    \'Did you correctly initalize a `fig` object using `fig = plt.figure()`?\'\n\ndef test_y_axis():\n    assert (sorted(stu_yaxis) == y_axis_data).all(), \\\n    \'Are you correctly plotting viwership in millions on the y axis? Make sure you are calling your plot in the same cell that you initialize `fig`!\'\n    \ndef test_x_axis():\n    assert (sorted(stu_xaxis) == x_axis_data).all(), \\\n    \'Are you correctly plotting episode number on the x axis? Make sure you are calling your plot in the same cell that you initialize `fig`!\'\n    \ndef test_colors():\n    assert (len(stu_colors) == len(color_data)), \\\n    \'Are you correctly setting the colors according to the rating scheme provided? Make sure you are calling your plot in the same cell that you initialize `fig`!\'\n    assert (np.sort(color_data) == np.sort(stu_colors)).all() or \\\n    (np.sort(bonus_color_data) == np.sort(stu_colors)).all() or \\\n    (np.sort(bonus_color_data_2) == np.sort(stu_colors)).all(), \\\n    \'Are you correctly setting the colors according to the rating scheme provided? Make sure you are calling your plot in the same cell that you initialize `fig`!\'\n\ndef test_size():\n    assert (len(stu_sizes) == len(size_data)), \\\n    \'Are you correctly plotting all points as size 25, except for guest-star episodes which are sized at 250? Make sure you are calling your plot in the same cell that you initialize `fig`!\'\n    assert all(size_data == np.sort(stu_sizes)), \\\n    \'Are you correctly plotting all points as size 25, except for guest-star episodes which are sized at 250? Make sure you are calling your plot in the same cell that you initialize `fig`!\'\n\ndef test_labels():\n    assert (title.lower() == (\'Popularity, Quality, and Guest Appearances on the Office\').lower()), \\\n    \'Did you set the correct title? Make sure you are specifying your plot in the same cell that you initialize `fig`!\'\n    assert (x_label.lower() == (\'Episode Number\').lower()), \\\n    \'Did you set the correct x label? Make sure you are specifying your plot in the same cell that you initialize `fig`!\'\n    assert (y_label.lower() == (\'Viewership (Millions)\').lower()), \\\n    \'Did you set the correct x label? Make sure you are specifying your plot in the same cell that you initialize `fig`!\' \n\ndef test_stars():\n    assert (top_star == \'Cloris Leachman\' or top_star == \'Jack Black\' or top_star == \'Jessica Alba\'), \\\n    "Are you correctly assigning one of the guest stars of the most popular episode to `top_star`?"')

