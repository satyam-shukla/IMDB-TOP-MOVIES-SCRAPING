import json,requests
from bs4 import BeautifulSoup
with open("task1_top_movies.json", 'r') as file:
    d_top_250_movies=json.load(file)

list_of_top_250_movies=[]
shi=0
for movie in d_top_250_movies["top_250_movies"]:
    ### MOVIE LINK
    m_link=movie["url"]

    page=requests.get(m_link)
    soup=BeautifulSoup(page.text,"html.parser")

    ### MOVIE TIME
    m_time=soup.find('div',class_="TitleBlock__TitleMetaDataContainer-sc-1nlhx7j-2 hWHMKr").text
    time=m_time[-8:]
    m=''
    try:
        for l in time:
            if l.isdigit():
                m+=l
        movie['Runtime']=f'{int(m[0])*60+int(m[1:])}'+' min'
    except:
        movie['Runtime']=f'{int(m[0])*60}'+' min'
    # print(movie)

    ## MOVIE POSTER
    p_link=soup.find("a",class_="ipc-lockup-overlay ipc-focusable")["href"]
    poster_url="https://www.imdb.com"+p_link
    movie['poster url']=poster_url

    ### MOVIE GENERICS
    genre_movie=[]
    try:
        genre=soup.find("div",class_="ipc-chip-list GenresAndPlot__GenresChipList-cum89p-4 gtBDBL")
        for i in genre:
            li=i.get_text()
            genre_movie.append(li)
    except:
        genre_movie.append('unable to find path')
    movie['generics']=genre_movie

    ### MOVIE DIRECTOR
    dire=[]
    director=soup.find("div",class_="ipc-metadata-list-item__content-container").find("ul")
    for i in director:
        a=i.get_text()
        dire.append(a)
    movie['Director']=dire

    ### MOVIE COUNTRY,LANGUAGE
    m_details=soup.find('ul',class_="ipc-metadata-list ipc-metadata-list--dividers-all ipc-metadata-list--base")
    details= m_details.find_all('li', class_='ipc-metadata-list__item')
    for det in details:
        if "Country of origin" in det.text:
            c=det.text
            country=c[17:]
        if "Language" in det.text:
            l=det.text
            language=l[8:]
    movie['country']=country
    movie['language']=language

    ### MOVIE STORYLINE
    story=soup.find('span',class_="GenresAndPlot__TextContainerBreakpointXS_TO_M-cum89p-0 dcFkRD").text
    movie['story line']=story
    # print(movie)
    shi=shi+1 
    print(shi) 
    list_of_top_250_movies.append(movie)
with open("D_of_250_M.json","w") as file:
    json.dump(list,file,indent=4)
    file.close()







