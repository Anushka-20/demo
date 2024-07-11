# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 10:42:34 2024

@author: anush
"""

import matplotlib.pyplot as plt

# Data from the image
countries = ['Pakistan', 'Sri Lanka', 'Australia', 'Australia', 'Australia', 'India', 'Australia', 'England', 'Australia']

# Manually count the number of wins for each country
win_counts = {
    'Pakistan': countries.count('Pakistan'),
    'Sri Lanka': countries.count('Sri Lanka'),
    'Australia': countries.count('Australia'),
    'India': countries.count('India'),
    'England': countries.count('England')
}

# Data for the pie chart
labels = list(win_counts.keys())
sizes = list(win_counts.values())
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

# Explode: pull out the slices
explode = (0.1, 0.1, 0.1, 0.1, 0.1)  # Adjust the values to emphasize each slice

# Plot the pie chart
plt.figure(figsize=(10, 6))
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors)

# Add a title
plt.title('Cricket World Cup Wins by Country (1992-2023)')

# Display the pie chart
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
