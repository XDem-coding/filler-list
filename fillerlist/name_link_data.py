def name_link():
    from requests import get
    from bs4 import BeautifulSoup
    from pickle import dump

    main_data = []
    id = 0
    soup = BeautifulSoup(get('https://www.animefillerlist.com/shows').text)

    groups = soup.find_all('div', {'class': 'Group'})
    for group in groups:
        elements = group.find_all('a')
        for element in elements:
            link = f'https://www.animefillerlist.com{element.get("href")}'
            main_data.append({'link': link, 'name': element.text, 'id': id})
            id += 1

    with open('name_link_data.txt','wb') as f:
        dump(main_data, f)
