
from decimal import DivisionByZero
from lib2to3.pgen2 import driver
from msilib.schema import tables
from select import select
from tkinter import Button
from tkinter.tix import DirSelectBox
from xml.dom.minidom import Element
from selenium import webdriver
import pyautogui as pg

from time import sleep
from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui as pg
import requests
import pandas as pd
from bs4 import BeautifulSoup
import json

ra=pg.prompt("Digite seu RA:")
senha=pg.prompt("digite sua senha:")
options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome('chromedriver.exe',chrome_options=options)
driver.get("http://waewebsantos.esamc.br/waeweb/servlet/hwalgn?21")
driver.find_element(By.ID,"vUSUARIO").send_keys(ra)
driver.find_element(By.ID,"vSENHA").send_keys(senha)
driver.find_element(By.ID, "BTNOK").click()
sleep(2)


#element=WebDriverWait(driver,10).until(
#    EC.presence_of_element_located((By.LINK_TEXT,"http://waewebsantos.esamc.br/waeweb/servlet/hnwabol")))
driver.get("http://waewebsantos.esamc.br/waeweb/servlet/hnwabol")
element=driver.find_element(By.XPATH,('/html/body/form/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr[4]/td/table/tbody/tr/td/div/table[1]/tbody/tr[2]/td/table'))
htmlcontent=element.get_attribute('outerHTML')
soup= BeautifulSoup(htmlcontent,'html.parser')
table=soup.find(id='BoletimSbf')
df=pd.read_html(str(table))[0].head(10)
print(df)


sleep(100)