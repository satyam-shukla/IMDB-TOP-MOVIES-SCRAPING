import json
with open("D_of_250_M.json","r") as file:
    data=json.load(file)
movie_details_list=[]
for i in data[:10]:
    movie_details_list.append(i)
with open("task5_.json","w") as shi:
    json.dump(movie_details_list,shi,indent=4)
    shi.close()


