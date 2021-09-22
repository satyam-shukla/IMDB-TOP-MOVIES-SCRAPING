import json
with open("task5_.json","r") as file:
    data=json.load(file)
c,b=0,0
for i in data:
    bb=i["language"]
    if "Malayalam" in bb:
        c+=1
    if "Hindi" in bb:
        b+=1
lang=["malayalam","hindi"]
ff=[c,b]
langu=dict(zip(lang,ff))
with open("task_6.json","w") as file:
    json.dump(langu,file)
    file.close()

            