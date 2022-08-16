import requests
from bs4 import BeautifulSoup as BS

with open('films_in_rating.txt', 'r+', encoding='UTF-8') as file:
    req = requests.get("https://www.kinoafisha.info/rating/releases/")
    html = BS(req.content, 'html.parser')
    rat = html.find('div', class_='site_content')
    cont = rat.find_all('a')

    lst_movie = []

    if (len(cont)):
        for elem in cont:
            lst_movie.append(elem.text.strip())
        print(' '.join(lst_movie[12:205]), sep='', end='\n')

    else:
        print('No')

    file.write(str(' '.join(lst_movie[12:205])))