import tkinter
from tkinter import Label
from selenium import webdriver
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import os
import string
import random
from Tkinter import *

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)

def programa() :


    url = "https://www.fgc.cat/es/buscador/?from_address=Sant+Joan&from_lat=41.490153877&from_lng=2.076498641&from_code=SJ&to_address=Sant+Cugat&to_lat=41.467910377&to_lng=2.078203288&to_code=SC&datetime_option=0&range_option=0&date=06-10-2021&time_from=16%3A57&transport=0"
    driver.get(url)

    info = driver.find_element_by_xpath("//*[@id='trips-timetable']").text
    llista = info.split("\n")

    for i in range(0, 3):
        llista.remove(llista[0])
    for i in llista:
        if llista.index(i) % 2 == 0:
            llista.remove(i)
    new_list = " ".join(llista)

    return new_list


    

texto = programa()
root = tkinter.Tk()
root.title('Trens FGC')
root.geometry('1920x1080')

label = Label(root,text=texto)
label.pack()
label.config(font=("Verdana", 78))

root.mainloop()