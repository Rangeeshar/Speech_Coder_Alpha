from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import json
import pyautogui as mouse
from bs4 import BeautifulSoup
from Naked.toolshed.shell import execute_js
driver=webdriver.Chrome()
success = execute_js('C:\\Users\\user\\Desktop\\SpeechRecongnizer\\houndify-web-sdk\\houndify-web-sdk\\example\\server.js')
time.sleep(3)
driver.get("C:\\Users\\user\\Desktop\\SpeechRecongnizer\\Login\\index.html")
i,flag=0,0
'''while(i<=20):
    i+=1
    time.sleep(2)
    print(mouse.position())'''
while(True):
    b=driver.current_url
    if (b.strip()=="http://localhost:3446/?"):
        row=58
        column=574
        while(True):
            flag=1
            time.sleep(12)
            elem=driver.find_element_by_id("responseJSON")
            val=elem.get_attribute("value")
            actual=json.loads(val)
            data=actual['AllResults'][0]['SpokenResponse']
            data=data.strip()
            if(data=="run"):        
                mouse.click(217,285)
                time.sleep(8)
                break
            elif data=="terminate":
                break
            else:
                mouse.moveTo(row,column,duration=0.55)
                mouse.click(row,column,button='left')
                mouse.typewrite(data+"\n")
                column+=15
                time.sleep(11)
                mouse.click(148,219)
    i+=1
    time.sleep(5)
    if i==3 or flag==1:
        break
    


        


    


