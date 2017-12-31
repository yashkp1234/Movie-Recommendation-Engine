## Yagnik Patel
## 2017-12-23
## Good Movie Analysis

## Import Packages
import pandas as pd   #importing all the important packages
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import json

## Define dataset
df = pd.read_csv('movies_metadata.csv', encoding = 'UTF-8', low_memory=False)

## Filter Movies with more than 100 reviews and less than 40 minutes of runtime
df_fil = df[df["vote_count"] >= 100]
df_fil2 = df_fil[df_fil["runtime"] >= 40]
movie_data = df_fil2[df_fil2["runtime"] <= 180]

## Graph Runtime vs Ratings
g = sns.lmplot(x = "runtime", y = "vote_average", data = movie_data,
           size = 6, palette = "BuPu", hue = "runtime", fit_reg=False,
           legend = False)
plt.title("Runtime in Relation to Ratings")
plt.subplots_adjust(top = 0.95)

## Graph popularity and vs Ratings
f = sns.lmplot(x = "popularity", y = "vote_average", data = movie_data,
               size = 6, fit_reg=False, legend = False)
f.set(xticklabels = [])
plt.title("Popularity in Relation to Ratings")
plt.subplots_adjust(top = 0.95)
plt.show()





