def writer():
    from pickle import dump, load
    input('You really want to run this??')
    confirmation = input('If so please provide the confirmation (YES)')
    if confirmation == 'YES':
        print('IDENTITY CONFIRMED')
        input('Just one last enter for security purposes')
        main_data = []

        with open('name_link_data.txt', 'rb') as f:
            data = load(f)

        links = [element['link'] for element in data]

        for link in links:
            main_data.append({"link": link, "image":None, "background": None})

        with open('image_data.txt', 'wb') as f:
            dump(main_data, f)
    else:
        print('MISSION ABORT')


def checker():
    from pickle import dump, load
    with open('name_link_data.txt', 'rb') as f:
        data1 = load(f)

    with open('image_data.txt', 'rb') as f:
            data2 = load(f)

    data1_links = [element['link'] for element in data1]
    data2_links = [element['link'] for element in data2]

    not_in_list = [j for i, j in zip(data1_links, data2_links) if i != j]
    print(not_in_list)
