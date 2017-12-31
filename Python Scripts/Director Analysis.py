## Yagnik Patel
## 2017-12-23
## Good Movie Analysis

## Import Packages
import pandas as pd   #importing all the important packages
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import json
from ast import literal_eval


## Define dataset
df = pd.read_csv('movies_metadata.csv', encoding = 'UTF-8', low_memory=False)
df2 = pd.read_csv('credits.csv', encoding = 'UTF-8', low_memory=False)

## Filter Movies with more than 100 reviews and less than 40 minutes of runtime
df_fil = df[df["vote_count"] >= 100]
df_fil2 = df_fil[df_fil["runtime"] >= 40]
movie_data = df_fil2[df_fil2["runtime"] <= 180]


def get_director(x):
    for i in x:
        if i['job'] == 'Director':
            return i['name']
    return "None"

## 
movie_data['id'] = movie_data['id'].astype('int')
df2['id'] = df2['id'].astype('int')
df2['crew'] = df2['crew'].apply(literal_eval)
df2['director'] = df2['crew'].apply(get_director)
movie_data = movie_data.merge(df2, on='id')

def remove_dups (list_ex):
    already_seen = []
    for x in range(0, len(list_ex)):
        if list_ex[x] != "None" and list_ex[x] not in already_seen:
            already_seen.append(list_ex[x])
    return already_seen

directors = movie_data['director']
title = movie_data['title']
ratings = movie_data['vote_average']
directors2 = np.array(directors)
dir_fil = remove_dups(directors2)
dir_ave_rate = []


def round_two (floating):
    return float(format(floating, ".2f"))

def get_dir_ave (dir_name):
    indices = np.where(directors2 == dir_name)[0]
    total = 0
    for x in range(0, len(indices)):
        index = indices[x]
        total = total + ratings[index]
    return (total / len(indices))

for x in range(0, len(dir_fil)):
    average = get_dir_ave(dir_fil[x])
    dir_ave_rate.append(round_two(average))

mean_rating = round_two(np.array(dir_ave_rate).mean())
sample_dir = []
sample_ave = []


for x in range(0, len(dir_fil)):
    if x % 21 == 0:
        sample_dir.append(dir_fil[x])
        sample_ave.append(dir_ave_rate[x])

sample_dir.append("Mean Rating")
sample_ave.append(mean_rating)

f = sns.barplot(x = sample_dir, y = sample_ave)
f.set_xticklabels(sample_dir, rotation=90)
f.set_title("Directors Average Film Rating", size = 30)
f.set_ylabel("Average Film Rating", size = 15)
f.set_xlabel("Director", size = 15)
             
plt.subplots_adjust(bottom = 0.24)

mng = plt.get_current_fig_manager()
mng.window.state('zoomed') 
plt.show()

def movie_displayer (dire):
    apple = np.where(directors2 == dire)[0]
    for x in apple:
        print(title[x], ratings[x], directors[x], x)





        




                           
    
    
        
                   



