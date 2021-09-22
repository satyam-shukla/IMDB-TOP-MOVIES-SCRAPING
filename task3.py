import json
with open("task2_same_year.json", 'r') as file:
    x=json.load(file)
def group_by_decade(l):     #task3
   did={}
   ss=set()
   for i in l:
       ss.add(int(i)//10)    
   for j in ss:
       ll=[]
       for k in l:
           if str(j) in str(k):
               for  a in l[k]:
                   ll.append(a)
       did[f'{j}0']=ll
   ff=open('group_by_decede.json',"w")
   json.dump(did,ff,indent=4)
   ff.close()   
group_by_decade(x)
