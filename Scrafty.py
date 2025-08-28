import os
import sys
import requests
from bs4 import BeautifulSoup
os.system('clear')

def Input():
    link=str(input("enter the link"))
    mode=str(input("enter the tag name (default is p)"))
    if(mode==''):
        mode='p'
    try:
        req = requests.get(link).text

    except requests.exceptions.RequestException as e:
        print("Invalid Input:", e)
        if(input('try again?(y/n)')=='y'):
            os.system('clear')
            Input()
        
    
    return [req,mode]







def Scrap(req,mode):
    txt=''
    soup=BeautifulSoup(req,'lxml')
    text= soup.find_all(mode)
    print(text)
    for i in text:
        txt=txt+(i.text.strip()+'\n\n')
    
    output.write(txt)




    
output=open('output.txt','w+')
input=Input()

Scrap(*input)


output.close()