from time import time
from task1 import*
import os,json
with open("D_of_250_M.json","r") as file:
    data=json.load(file)
def scrap_id_movie(id):
    for i in id:
        url=i["url"][27:-1]+".json"
        if not(os.path.exists(url)):
            print("yes")
            file=open(f"{url}","w+")
            c=json.dump(i,file,indent=4)
            file.close()
        else:
            print("file is already there")
scrap_id_movie(data)
