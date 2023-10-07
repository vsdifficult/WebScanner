from bs4 import BeautifulSoup 

import requests 




    
def dirsearch(self, url) :
        response = requests.get(url)
        if response.status_code == 200:
            content = response.text
            dirs = []
            files = []
            for line in content.splitlines():
                if 'href="' in line:
                    path = line.split('href="')[1].split('"')[0]
                    if path.endswith('/'):
                        dirs.append(path)
                    else:
                        files.append(path)
        
            print("Directories:")
            for d in dirs:
                print("[*]"+d)
        
            print("\nFiles:")
            for f in files:
                print("[*]"+f)
        else:
               print("Error: ", response.status_code) 
 
def webkit_scaner(url, name): 
       response = requests.get(url)
        
       if response.status_code == 200: 
            soup = BeautifulSoup(response.text, 'html.parser')
    
            # Поиск <a> тегов, которые содержат указанное имя
            found_elements = soup.find_all('a', string=name)
    
            # Перебор найденных элементов и вывод их атрибутов
            for element in found_elements:
                print('Ссылка:', "[*]"+element)
                print('Текст:', element.text)
                print('---')  
       else: 
            print("Erorr:", response.status_code)