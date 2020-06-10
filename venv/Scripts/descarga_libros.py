# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 14:18:05 2020

@author: user
"""

import requests
from selenium import webdriver  
import codecs
from bs4 import BeautifulSoup as bs
import re
import requests
import pandas as pd

# list containing the books

directorio=pd.read_csv(direct+'directorio.csv',encoding='unicode_escape')
## i ned to set driver
driver = webdriver.Chrome("C:/Users/user/Desktop/libros/chromedriver.exe")
## our main function call take_the book relie under two parameters
## first wee need the site where the download link is hosted

## second we need the folder in our system that we want store al the books

def get_direct_link(pagina):

    
    driver.get(pagina)
    content=driver.page_source
    soup=bs(content,'html.parser')
 
    links=[]
    
    base_link='http://link.springer.com'
    
    for a in soup.find_all('a',href=True):
        links.append(a.get('href'))
    
    candidatos=[]
    for i in range(0,len(links)):
        if (re.match(r'/content/pdf/.+',links[i])==None):
            None 
        else: 
            candidatos.append(re.match(r'/content/pdf/.+',links[i]))
    
    return base_link+candidatos[0].group(0)

enlace=get_direct_link(pagina=pagina)


   

def get_book(link,file):
    
    r = requests.get(link, stream=True)
    
    direct='C:/Users/user/Desktop/libros/'+file
    
    with open(direct, 'wb') as f:
        f.write(r.content)    
        
 
def take_the_book(pagina,file):
    
    link=get_direct_link(pagina=pagina)
    
    get_book(link=link,file=file)

for i in range(1,len(directorio)):
    pagina=directorio.iloc[i]['OpenURL']
    file= str (i)+'.pdf'
    take_the_book(pagina=pagina,file=file)