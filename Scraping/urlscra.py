from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://www.eltiempo.com/'
page  = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

text = soup.get_text()

remove = ",;:.\n!\"'"
for charter in remove:
    text = text.replace(charter,"")
    text = text.lower()
    words = text.split(" ")
    diccionary_frecuency = {}
    for word in words:
        if word in diccionary_frecuency:
            diccionary_frecuency[word] += 1
        else:
            diccionary_frecuency[word] = 1

    for word in diccionary_frecuency:
        frecuency = diccionary_frecuency[word]
        print(f"Esta palabra '{word}' se repite {frecuency}" ' ' 'vez')