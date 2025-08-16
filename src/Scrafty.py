import os
import sys
import requests
from bs4 import BeautifulSoup
os.system('clear')

def Input():
    link=str(input("enter the link"))
    mode=str(input("enter the tag name (default is p)"))
    if(mode==''):mode='p'
    try:
        link_a = requests.get(link)

    except requests.exceptions.RequestException as e:
        print("Invalid Input:", e)
        if(input('try again?(y/n)')=='y'):
            os.system('clear')
            Input()
        
    
    return [link_a,mode]

def Scrap(link_a,mode):
    txt=''
    soup=BeautifulSoup(link_a.text,'lxml')
    text= soup.find_all(mode)

    for i in text:
        txt=txt+(i.text.strip()+'\n\n')

    output.write(txt)
    
output=open('output.txt','w+')
input=Input()

Scrap(input[0],input[1])


output.close