from tkinter import * 
import tkinter as tk
from bs4 import BeautifulSoup 

import requests


global value


def dirsearch() : 
        v_b = value.replace("'", "")
        response = requests.get(v_b)
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
        
            
            for d in dirs:
                output_text.insert(tk.END, f"[*] {d}" + '\n')
        
     
            for f in files:
              
                output_text.insert(tk.END, f"[*] {f}" + '\n')
       
        else:
               print("Error: ", response.status_code) 
 
# def webkit_scaner(url, name): 
#        response = requests.get(url)
        
#        if response.status_code == 200: 
#             soup = BeautifulSoup(response.text, 'html.parser')
    
#             # Поиск <a> тегов, которые содержат указанное имя
#             found_elements = soup.find_all('a', string=name)
    
#             # Перебор найденных элементов и вывод их атрибутов
#             for element in found_elements:
#                 print('Ссылка:', "[*]"+element)
#                 print('Текст:', element.text)
#                 print('---')  
#        else: 
#             print("Erorr:", response.status_code)






window = tk.Tk()

window.title("Web Scanner")
window.geometry("400x300") 
window.resizable(False, False)

lv = Label(text="URL:").pack()

entry = tk.Entry(window)
entry.pack()

value = entry.get()

button = tk.Button(window, text="Connect", command=dirsearch)
button.pack()

output_text = tk.Text(window)
output_text.pack()

window.mainloop()