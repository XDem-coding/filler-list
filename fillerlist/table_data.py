def table():
    from pickle import load, dump
    from requests import get
    from bs4 import BeautifulSoup

    with open('name_link_data.txt', 'rb') as file:
        data = load(file)

    links = [element['link'] for element in data]
    main_data =[]


    for link in links:
        source_code = get(link).text
        soup = BeautifulSoup(source_code)

        description = soup.find('div', {'class': 'Description'}).find('p').text
        
        numbers = soup.find_all('td', {'class': 'Number'})
        title = soup.find_all('td', {'class': 'Title'})
        type_ = soup.find_all('td', {'class': 'Type'})

        numbers_text = [i.text for i in numbers]
        title_text = [i.text for i in title]
        type_text = [i.text for i in type_]

        main_data.append({"link": link, "description":description , "number": numbers_text, "title": title_text, "type": type_text})
        print(f'Done {links.index(link)}')

    with open('table_data.txt', 'wb') as f:
        dump(main_data, f)

