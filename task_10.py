from task5 import *
import json
with open("D_of_250_M.json","r") as file:
    data=json.load(file)
def scrape_director_details(movies):
    lang_dic={}
    for i in movies:
        for director in i['Director']:
            lang_dic[director]={}
    for i in range(len(movies)):
        for director in lang_dic:
            if director in movies[i]['Director']:
                for language in movies[i]['language']:
                    lang_dic[director][language]=0
    for i in range(len(movies)):
        for director in lang_dic:
            if director in movies[i]['Director']:
                for language in movies[i]['language']:
                    lang_dic[director][language]+=1
    return lang_dic
    a=open("task100.json","w")
    b=json.dump(lang_dic,a,indent=4)
    a.close()
print(scrape_director_details(data))