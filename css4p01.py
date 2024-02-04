#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: ssalie
"""
#%%
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt

#%%
df = pd.read_csv("movie_dataset.csv"

#%% cleaning data

df.columns = df.columns.str.replace(' ', '_')
df.fillna(df.mean(),inplace=True)

#%%
highest_rated_movie = df.loc[df['Rating'].idxmax(), 'Title']

#%%
ave_revenue = df["Revenue_(Millions)"].mean()

#%% 
start_year = 2015
end_year = 2017

df_2015_2017 = df[(df['Year'] >= 2015) & (df['Year'] <= 2017)]
avg_revenue_2015_2017 = df_2015_2017['Revenue_(Millions)'].mean()

#%%
df_2016 = df[df['Year'] == 2016]
movies_2016 = len(df_2016)

#%% 
df_nolan = df[df['Director'] == "Christopher Nolan"]
movies_nolan = len(df_nolan)

#%%
df_rating = df[df['Rating'] >= 8.0]
movies_rating = len(df_rating)

#%%
median_nolan = df_nolan['Rating'].median()

#%%
df_average_rating_year = df.groupby('Year')['Rating'].mean()
highest_average_rating_year = df_average_rating_year.idxmax()

#%%
df_2006 = df[df['Year'] == 2006]
df_2016 = df[df['Year'] == 2016]
perc_increase = ((len(df_2016) - len(df_2006)) / len(df_2006)) * 100

#%%
all_actors = df['Actors'].str.split(', ')
most_common_actor = pd.Series(all_actors.sum()).mode()[0]

#%%
df['Genre_List'] = df['Genre'].str.split(', ')
df_exploded = df.explode('Genre_List')

all_genres_list = df_exploded['Genre_List'].tolist()

unique_genres = []

for item in all_genres_list:
    # Split the string based on commas
    elements = item.split(',')
    
    # Extend the new list with the resulting elements
    unique_genres.extend(elements)
num_unique_genres = len(set(unique_genres))

#%%
corr_matrix = df.corr()

