import json
with open("task5_.json","r") as file:
    data=json.load(file)
a=[]
for i in data:
    cc=i["Director"]
    a.append(cc)
with open("task_7.json","w") as file:
    json.dump(a,file)
    file.close()