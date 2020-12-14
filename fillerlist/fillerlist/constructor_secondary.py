from pickle import load


def constructor(anime_name, description, number, title, type, image, background):

    code1 = f'''
    <!DOCTYPE html>
    <html>

    <head>
        <link href="https://unpkg.com/tailwindcss@^1.0/dist/tailwind.min.css" rel="stylesheet">
        <title>{anime_name}</title>'''

    style = '''
        <style>
            header{
                position: sticky;
                top: 0px;
            }

            .blur{
                background-color: rgba(0, 0, 0, 0.6);
                border-radius:30px;
            }
            
            .bg{
                background-repeat: no-repeat;
                background-size: cover;
            }

            .filler{
                color: #ff6666;
            }

            .canon{
                color: #66ff66;
            }

            td{
                font-weight: bold;
            }

            .table-sortable th {
                    cursor: pointer;
                }

                .table-sortable .th-sort-asc::after {
                    content: "\\25b4";
                }

                .table-sortable .th-sort-desc::after {
                    content: "\\25be";
                }

                .table-sortable .th-sort-asc::after,
                .table-sortable .th-sort-desc::after {
                    margin-left: 5px;
                }

                .table-sortable .th-sort-asc,
                .table-sortable .th-sort-desc {
                    background: rgba(0, 0, 0, 0.1);
                }
            
            footer div div a{
			    padding: 10px;
			    margin: auto;
		    }
            
        </style>'''

    code2 = f'''</head>

    <body>
        <header class="text-gray-500 bg-gray-900 body-font">
            <div class="container mx-auto flex flex-wrap p-5 flex-col md:flex-row items-center">
                <a
                    class="mx-auto flex order-first lg:order-none lg:w-1/5 title-font font-medium items-center text-white lg:items-center lg:justify-center mb-4 md:mb-0 text-xl">
                    <svg height="30" viewBox="0 0 512 512" width="30">
                        <g>
                            <g>
                                <circle cx="256" cy="256" fill="#ffb54a" r="256" />
                            </g>
                            <path
                                d="m511.371 273.846-154.861-154.861-192.408 6.405-8.612 267.625 118.356 118.356c127.159-8.758 228.767-110.366 237.525-237.525z"
                                fill="#f9880d" />
                            <path d="m356.51 118.985v58h-143.02v57.3h143.02v58h-143.02v100.73h-58v-274.03z"
                                fill="#f8fffb" />
                            <path d="m256 118.98h100.51v58h-100.51z" fill="#d8d8d8" />
                            <path d="m256 234.28h100.51v58h-100.51z" fill="#d8d8d8" />
                            <g>
                                <path d="" fill="#f8fffb" />
                            </g>
                        </g>
                    </svg> iller List
                </a>
            </div>
        </header>

        <section class="bg text-gray-400 bg-gray-800 body-font" style="background-image: url('{background}');">
            <div class="container mx-auto flex px-5 py-10 md:flex-row flex-col items-center">
                <div class="lg:max-w-lg lg:w-full md:w-1/2 w-5/6 md:mb-0 mb-10">
                    <img class="object-cover object-center rounded" alt="Anime poster" src="{image}" width="200" height="50">
                </div>
                <div
                    class="blur lg:flex-grow md:w-1/2 flex flex-col md:items-start md:text-left items-center text-center py-10 px-10">
                    <h1 class="title-font sm:text-4xl text-3xl mb-4 font-medium text-white">{anime_name}</h1>
                    <p class="mb-8 leading-relaxed">{description}</p>
                    <a href="https://www.animefillerlist.com/" target="_blank" class="mb-8 leading-relaxed">Source: animefillerlist.com</a>
                </div>
            </div>
        </section>

        <section class="text-gray-500 bg-gray-900 body-font">
            <div class="container px-5 py-24 mx-auto">
                <div class="lg:w-3/3 w-full mx-auto overflow-auto">
                    <table class="table-auto w-full text-center table-sortable">
                        <thead>
                            <tr>
                                <th class="px-4 py-3 title-font tracking-wider font-medium text-white text-sm bg-gray-800 rounded-tl rounded-bl">
                                    Number</th>
                                <th class="px-4 py-3 title-font tracking-wider font-medium text-white text-sm bg-gray-800">
                                    Title</th>
                                <th class="px-4 py-3 title-font tracking-wider font-medium text-white text-sm bg-gray-800 rounded-tr rounded-br">
                                    Type</th>
                            </tr>
                        </thead>
                        <tbody>

    '''
    code3 = ''

    for i in range(0, len(number)):
        if str(type[i]) == 'Filler':
            code3 += f'''
            <tr>
                <td class="filler px-4 py-3 border-b-2 border-gray-800 text-lg1">{number[i]}</td>
                <td class="filler px-4 py-3 border-b-2 border-gray-800 text-lg1">{title[i]}</td>
                <td class="filler px-4 py-3 border-b-2 border-gray-800 text-lg1-center">{type[i]}</td>
            </tr>
        '''
        else:
            code3 += f'''
            <tr>
                <td class="canon px-4 py-3 border-b-2 border-gray-800 text-lg1">{number[i]}</td>
                <td class="canon px-4 py-3 border-b-2 border-gray-800 text-lg1">{title[i]}</td>
                <td class="canon px-4 py-3 border-b-2 border-gray-800 text-lg1-center">{type[i]}</td>
            </tr>
        '''

    code4 = '''
                            </tbody>
                    </table>
                </div>
            </div>
        </section>


     <footer>
        <div class="bg-gray-800">
        <div class="container px-5 py-6 mx-auto flex items-center sm:flex-row flex-col">
        <a href="https://anilist.co/" target="_blank" class="flex title-font font-medium items-center md:justify-start justify-center text-white">
            Image source: anilist.co
        </a>
        <a class="flex title-font font-small items-center md:justify-start justify-center text-gray-600 mx-10px">
            I do not claim any ownership of the data shown on the website
        </a>
        <a class="flex title-font font-medium items-center md:justify-start justify-center text-white">
            Email: xdotaku80@gmail.com
        </a>
        </div>
        </div>
    </footer>

    </body>

    <script>
            function sortTableByColumn(table, column, asc = true) {
            const dirModifier = asc ? 1 : -1;
            const tBody = table.tBodies[0];
            const rows = Array.from(tBody.querySelectorAll("tr"));

            const sortedRows = rows.sort((a, b) => {
            const aColText = a.querySelector(`td:nth-child(${ column + 1 })`).textContent.trim();
            const bColText = b.querySelector(`td:nth-child(${ column + 1 })`).textContent.trim();
            if (isNaN(parseFloat(aColText)) && isNaN(parseFloat(bColText))) {
                return aColText > bColText ? (1 * dirModifier) : (-1 * dirModifier);
            }
            return +aColText > +bColText ? (1 * dirModifier) : (-1 * dirModifier);
            });

            while (tBody.firstChild) {
                tBody.removeChild(tBody.firstChild);
            }

            tBody.append(...sortedRows);

            table.querySelectorAll("th").forEach(th => th.classList.remove("th-sort-asc", "th-sort-desc"));
            table.querySelector(`th:nth-child(${ column + 1})`).classList.toggle("th-sort-asc", asc);
            table.querySelector(`th:nth-child(${ column + 1})`).classList.toggle("th-sort-desc", !asc);
            }

        document.querySelectorAll(".table-sortable th").forEach(headerCell => {
            headerCell.addEventListener("click", () => {
                const tableElement = headerCell.parentElement.parentElement.parentElement;
                const headerIndex = Array.prototype.indexOf.call(headerCell.parentElement.children, headerCell);
                const currentIsAscending = headerCell.classList.contains("th-sort-asc");

                sortTableByColumn(tableElement, headerIndex, !currentIsAscending);
            });
            });
        </script>
        
        </html>
    '''

    code = str(code1) + str(style) + str(code2) + str(code3) + str(code4)

    return code


def infocollector(id):
    name_link_data = open('name_link_data.txt', 'rb')
    table_data = open('table_data.txt', 'rb')
    image_data = open('image_data.txt', 'rb')
        
    name_link_data = load(name_link_data)
    table_data = load(table_data)
    image_data = load(image_data)

    anime_name = name_link_data[id]['name']
    description = table_data[id]['description']
    number = table_data[id]['number']
    title = table_data[id]['title']
    type = table_data[id]['type']

    link = table_data[id]['link']

    for i in range(0, id+1):
        if link == image_data[i]['link']:
            index = i
            image = image_data[index]['image']
            background = image_data[index]['background']
            break
    else:
        image, background = None, None
        

    if image == None:
        image = 'https://lh3.googleusercontent.com/e4Gng2EuP2-im3XXFkG1rPqWZefcn81oV3837KKoYunSS4EaRyYANSzu8iDQe2DXqQC_Zx4dlGfE_dU7h6_T81yMQSSf46xOWfFLw1F5NOz5vGRYjuREfJKXy2dtbEhzhcX-WFe7wsPP90XV_zmN1Av1ZQsrJFA7t40yzgT87sWt02toyXVuxgf19kMDbKjsFg9_-xs9qNbO9S0bF0FaUal4kwZpSV3Au6MN-RVEm492Ta235fD0TheuxMvgoYbTaoI0ZJ18Q8KtUEh266VzP3QHasXV4wtLDK5JhfhsT3bZQbZnCjUsFXq0jrVXFSNvsulXgFNehMmgecy1eVqXFBoFAr9AyqkTKquzVNMVG-2cWHM0ugG-fO7F1j5K-sWgOTkoxppWMRQJSS63VmGN7WZUSjEQeT5A1SAbB00IG_4Y2w4hGaIEC7RhtWybb4gkJxlK1l_KPhPS48OW3zY4g8xh40plKDfe-HK3tSnBaxSyq9wTbOCYngEPkXydBaCySWyIJ2X3L0imwvNQ8GoqPFb_JTdYK3j1LY0qOAZ9DlroMt5fCUtDEnhRoJQUpbtUMKgTnreVMdVeiKJP9SHZLSRv6R3eQJxEgUexVIQU5v26poCaI_IilJMQtFNJs182y5CXF_7ikQdodLQUrMBRQjH-7sLKfgkN9JA5bP20tMYVX47gExifyLLj-QE=s800-no?authuser=1'
    if background == None:
        background = 'none'

    code = constructor(anime_name, description, number, title, type, image, background)
    return code

