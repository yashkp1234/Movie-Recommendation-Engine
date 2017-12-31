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

def get_actors(x):
    list_acts = []
    for i in x:
        if i['order'] < 3:
            list_acts.append( i['name'] )
    if not list_acts:
        return list("None")
    else:
        return list_acts

## 
movie_data['id'] = movie_data['id'].astype('int')
df2['id'] = df2['id'].astype('int')
df2['cast'] = df2['cast'].apply(literal_eval)
df2['leads'] = df2['cast'].apply(get_actors)
movie_data = movie_data.merge(df2, on='id')


title = movie_data['title']
ratings = movie_data['vote_average']
leads = movie_data['leads']
act_ave_rate = []
np.leads = np.array(leads)

def round_two (floating):
    return float(format(floating, ".2f"))

def create_act_list ():
    act_ave = []
    count = []
    acts = []
    for x in range(0, len(leads)):
        if leads[0] != "None":
            for y in range(0, len(leads[x])):
                act = leads[x][y]
                if act not in acts:
                    acts.append(act)
                    count.append(1)
                    act_ave.append((ratings[x]))
                else:
                    index = acts.index(act)
                    count_ind = count[index]
                    count_ind += 1
                    act_ave[index] = (act_ave[index] + ratings[x]) / count_ind
    for x in range(0, len(act_ave)):                
        act_ave[x] = round_two(act_ave[x])                                       
    return [act_ave, acts]

act_and_ave = create_act_list()
actors = act_and_ave[1]
average = act_and_ave[0]
mean = round_two(np.array(average).mean())
sample_act = []
sample_ave2 = []


for x in range(0, len(actors)):
    if x % 60 == 0:
        sample_act.append(actors[x])
        sample_ave2.append(average[x])

sample_act.append("Mean Rating")
sample_ave2.append(mean)

f = sns.barplot(x = sample_act, y = sample_ave2)
f.set_xticklabels(sample_act, rotation=90)
f.set_title("Actors Average Film Rating", size = 30)
f.set_ylabel("Average Film Rating", size = 15)
f.set_xlabel("Actor", size = 15)
             
plt.subplots_adjust(bottom = 0.24)

mng = plt.get_current_fig_manager()
mng.window.state('zoomed') 
plt.show()







        
        
