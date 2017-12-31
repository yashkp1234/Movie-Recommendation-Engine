## Import Packages
import pandas as pd   #importing all the important packages
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import json
from ast import literal_eval
from operator import itemgetter

pd.options.mode.chained_assignment = None

## Define dataset
df = pd.read_csv('movies_metadata.csv', encoding = 'UTF-8', low_memory=False)
df2 = pd.read_csv('credits.csv', encoding = 'UTF-8', low_memory=False)
df3 = pd.read_csv('keywords.csv', encoding = 'UTF-8', low_memory=False)

## Filter Movies with less than 100 reviews and less than 40 minutes of runtime
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

def get_director(x):
    for i in x:
        if i['job'] == 'Director':
            return i['name']
    return "None"

def get_keywords(x):
    list_keywords = []
    for i in x:
        list_keywords.append(i['name'])
    return list_keywords

def get_collection(x):
    for i in x:
        return i['name']
    return "None"

def get_genres(x):
    list_genres = []
    for i in x:
        list_genres.append(i['name'])
    if not list_genres:
        return ["None"]
    else:
        return list_genres

## 
movie_data['id'] = movie_data['id'].astype('int')
movie_data['genres'] = movie_data['genres'].apply(literal_eval)
movie_data['genres'] = movie_data['genres'].apply(get_genres)
df2['id'] = df2['id'].astype('int')
df3['id'] = df3['id'].astype('int')
df2['cast'] = df2['cast'].apply(literal_eval)
df2['crew'] = df2['crew'].apply(literal_eval)
df2['director'] = df2['crew'].apply(get_director)
df2['leads'] = df2['cast'].apply(get_actors)
df3['keywords'] = df3['keywords'].apply(literal_eval)
df3['keywordz'] = df3['keywords'].apply(get_keywords)
movie_data = movie_data.merge(df2, on='id')
movie_data = movie_data.merge(df3, on='id')

titles = list(movie_data['title'])
keywords = list(movie_data['keywordz'])
directors = list(movie_data['director'])
leads = list(movie_data['leads'])
genres = list(movie_data['genres'])
collections = list(movie_data['belongs_to_collection'])
year = list(movie_data['release_date'])
adult = list(movie_data['adult'])
ratings = list(movie_data['vote_average'])
language = list(movie_data['original_language'])
directors2 = np.array(directors)

def retrieve_data (index):
    return [titles[index], directors[index], keywords[index],
            leads[index], genres[index], collections[index],
            year[index], adult[index], ratings[index], index, language[index]]

def scorer(data_list1, data_list2):
    score = 0
    year1 = int(str(data_list1[6])[0:4])
    year2 = int(str(data_list2[6])[0:4])
    if data_list1[1] == data_list2[1]: ## Same director
        indices = np.where(directors2 == data_list2[1])[0]
        if len(indices) > 5: ## Checks if director has made several movies
            score += 70 ## Higher score if so
        else:
            score += 40 ## Lower if not
    for x in data_list2[2]: ## Number of keywords that are the same
        if x in data_list1[2]: 
            score += 30
    for x in data_list2[3]: ## Number of actors that are the same
        if x in data_list1[3]:
            score += 30
    for x in data_list2[4]: ## Number of genres that are the same
        if x in data_list1[4]:
            score += 20
    if ("Family" in data_list1[4] or "family" in data_list1[2]) and "Family" not in data_list2[4]: ## Recommend Family Movies
        score -= 75
    if "Family" not in data_list1[4] and "Family" in data_list2[4]: ## Removes Family Moviess
        score -= 75
    if data_list1[4][0] == data_list2[4][0]: ## If main genre is the same
        score += 10
    if data_list1[5] == data_list2[5]: ## Movies belong to the same series
        if year1 > year2: ## Removes prequels
            score -= 300
        else:
            score += 50000 / ( (year2 - year1) * 7) ## Sequels recommended in order
    if  data_list1[7] == data_list2[7]: ## Adult nature check
        score += 100
    score += int(data_list2[8]) * 3 ## Scores movies of higher rating higher
    if data_list1[9] == data_list2[9]: ## Remove duplicate movies
        score -= 500
    if data_list1[10] == data_list2[10]: ## Scores movies of same language higher
        score += 100
    return score

def create_reccomendations(data_list1):
    scores = []
    for x in range(0, len(titles)):
        if data_list1[9] == x:
            scores.append([x, -1000])
        else:
            scores.append([x, scorer(data_list1, retrieve_data(x))])
    scores = sorted(scores, key = itemgetter(1), reverse = True)
    suggestions = []
    for x in range(0, 10):
        suggestions.append(scores[x])
    return suggestions
        
def engine(title):
    string = "\n"
    try:
        index = titles.index(title)
        list_data = retrieve_data(index)
        scores = create_reccomendations(list_data)
        movie_suggestions = []
        for x in scores:
            movie_suggestions.append(titles[x[0]])
        for x in range(0, len(movie_suggestions)):
            y = x + 1
            string = string + str(y) + ". " + str(movie_suggestions[x]) + "\n"
        return string
    except ValueError:
        string = "There is no movie of that name located in the database."
        return string

def question():
    x = str(input("\nEnter a movie you recently watched: "))
    output = engine(x)
    while output == "Error":
        x = str(input("\nThis movie is not in the database try again: "))
        output = engine(x)
    print(engine(x))

flag = False
while not flag:
        question()
        answer = str(input("These are your reccomendations!\n" + 
                           "To try again enter yes, to exit enter no: "))
        b_answer = ["no", "n", "exit", "close"]
        if answer.lower() in b_answer:
            print("Exiting")
            flag = True






                    
            
        










