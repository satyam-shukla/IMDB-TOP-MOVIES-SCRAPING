import requests,json
from bs4 import BeautifulSoup
url=requests.get("https://www.imdb.com/india/top-rated-indian-movies/")
soup=BeautifulSoup(url.text,"html.parser")
t_b=soup.find("tbody",{"class":"lister-list"}).findAll("tr")
p,l1,a_m=0,[],{}
for i in t_b:
    p+=1
    l=["position","movie_name","year","url","rating"]
    movie_name=i.find("td",{"class":"titleColumn"}).find("a").get_text()
    rating=i.find("td",{"class":"ratingColumn imdbRating"}).find("strong").get_text()
    year=i.find("td",{"class":"titleColumn"}).span.get_text()
    pr=year.replace("(","").replace(")","")
    prr=int(pr)
    link=i.find("td",{"class":"titleColumn"}).a["href"]
    urll="https://www.imdb.com"+link
    rating=float(rating)
    lst=[p,movie_name,prr,urll,rating]
    c=dict(zip(l,lst))
    l1.append(c)
    a_m.update({"top_250_movies":l1}) 
file=open("task1_top_movies.json","w")
json.dump(a_m,file,indent=4)
file.close()







