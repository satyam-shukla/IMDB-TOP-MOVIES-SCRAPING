import json
with open("task1_top_movies.json", 'r') as file:
    x=json.load(file)
task2={}
for i in x["top_250_movies"]:
    if i['year'] not in task2:
        task2[i['year']]=[]
for j in task2:
    for i in x["top_250_movies"]:
        if i['year']==j:
            task2[j].append(i)
file=open("task2_same_year.json","w")
json.dump(task2,file,indent=4)
file.close()

