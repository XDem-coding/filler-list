from pickle import load

def constructor():
    with open('name_link_data.txt', 'rb') as f:
        data = load(f)

    code1 = '''
    <!DOCTYPE html>
    <html>

    <head>
        <link href="https://unpkg.com/tailwindcss@^1.0/dist/tailwind.min.css" rel="stylesheet">
        <title>Naruto</title>
        <style>
            footer div div a {
                padding: 10px;
                margin: auto;
            }

            .searchBar {
                position: sticky;
                top: 0px;
            }
        </style>
    </head>

    <body>
        <header class="text-gray-500 bg-gray-800 body-font">
            <div class="container mx-auto flex flex-wrap p-20 flex-col md:flex-row items-center">
                <a class="mx-auto flex order-first lg:order-none lg:w-5/5 title-font font-medium items-center text-white lg:items-center lg:justify-center mb-4 md:mb-0 text-xl"
                    style="font-size:100px;">
                    <svg height="150" viewBox="0 0 512 512" width="150">
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

        <section class="text-gray-500 bg-gray-900 body-font">
            <div class="container px-5 py-24 mx-auto">
                <div class="flex flex-col text-center w-full mb-20">
                    <h1 class="sm:text-3xl text-2xl font-medium title-font mb-4 text-white">Anime list</h1>
                </div>

                <div class="searchBar container px-5 py-10 mx-auto bg-gray-900">
                    <div class="flex flex-wrap -m-2 mx-auto">
                        <input type="text" placeholder="Search" id="myinput" onkeyup="searchfnc()"
                            class="w-full bg-gray-800 rounded border border-gray-700 focus:border-indigo-500 text-base outline-none text-gray-100 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out">
                    </div>
                </div>
                '''

    code2 = ''

    for element in data:
        code2 += f'''
                    <div class="p-2 lg:w-3/3 md:w-2/2 w-full">
                        <div class="h-full flex items-center border-gray-800 border p-4 rounded-lg">
                            <div class="flex-grow">
                                <a href="/anime/id/{element['id']}/">
                                    <h2 class="aniName text-center text-white title-font font-medium">{element['name']}</h2>
                                </a>
                            </div>
                        </div>
                    </div>
                    '''
    code3 = '''        
                </div>
            </div>
        </section>


        <footer>
            <div class="bg-gray-800">
                <div class="container px-5 py-6 mx-auto flex items-center sm:flex-row flex-col">
                    <a href="#" class="flex title-font font-medium items-center md:justify-start justify-center text-white">
                        FILLERLIST
                    </a>
                    <a
                        class="flex title-font font-small items-center md:justify-start justify-center text-gray-600 mx-10px">
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
        const searchfnc = () => {
            let filter = document.getElementById('myinput').value.toLowerCase();

            let name = document.getElementsByClassName('aniName');

            for (let i = 0; i<name.length; i++) {
                let a = name[i]

                let textValue = a.textContent || a.innerHTML

                if(textValue.toLowerCase().indexOf(filter) > -1){
                    name[i].parentElement.parentElement.parentElement.parentElement.style.display = '';
                }else{
                    name[i].parentElement.parentElement.parentElement.parentElement.style.display = 'none';
                }
            }
            
        }
    </script>

    </html>
    '''

    code = code1 + code2 + code3

    return code
