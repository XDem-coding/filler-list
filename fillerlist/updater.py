from . import name_link_data
from . import table_data
from . import image_data
from pickle import load, dump


def up():
    while True:
        x = input('Upadte data: u\nCheck image_data.txt: c\nRead any file: r\nWrite image_data.txt: w\nUpdate image_data.txt: ui\nInput: ')

        if x == 'u':
            print('Updating name_link_data.txt')
            name_link_data.name_link()
            print('Updating table_data.txt and ofcourse gonna take a lot of time')
            table_data.table()
            print('Finally done bruh...')
            print('Done')

        if x == 'c':
            image_data.checker()

        elif x == 'r':
            file = input('File: ')
            with open(file, 'rb') as f:
                print(load(f))

        elif x == 'w':
            image_data.writer()

        elif x == 'ui':
            with open('image_data.txt', 'rb') as f:
                data = load(f)

            link_id = input('Update image, background for which link? ')
            for i in range(0, len(data)):
                if data[i]['link'] == link_id:
                    index = i
                    print('Found: ', data[i])
                    image_link = input('Image link: ')
                    background_link = input('Background link: ')
                    data[i]['image'] = image_link
                    data[i]['background'] = background_link

                    with open('image_data.txt', 'wb') as f:
                        dump(data, f)
                    print('Data updated')
                    break
            else:
                print('Entry not found with link:', link_id)
