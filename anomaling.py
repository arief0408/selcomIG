#import selenium
from selenium import webdriver
from time import sleep
import pandas as pd
import random
import os,sys
#directory chromedriver
chromedriver="chromedriver"

#deklarasi driver menggunakan chromedriver dan chrome
#driver=webdriver.Chrome(chromedriver)
#membuka halaman yang diinginkan
#driver.get("https:google.com")
username=input("Enter username: ")
password=input("Enter password: ")
tag=input("People that you want to mention/tag please use space after the tag so it doesnt messed up the tag (@ars @asd @adw ): ")
post_link=input("Instagram post url: ")
if getattr(sys,'frozen',False):
    chromedriver_path=os.path.join(sys._MEIPASS,"chromedriver.exe")
    driver=webdriver.Chrome(chromedriver_path)
else:
    driver=webdriver.Chrome()
class login():
    def __init__(self,username,password):
        self.driver=webdriver.Chrome(chromedriver)
        self.driver.get("https://instagram.com")
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')\
        .send_keys(username)                                                                                                                                   
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')\
        .send_keys(password)
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
        .click()
        print("login as",username)
        sleep(5)
        self.driver.get(post_link)
        sleep(4)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/article/div[3]/section[3]/div/form/textarea").click()
        self.repeat()
        
    def repeat(self):
        df=pd.read_excel('Book1.xlsx')
        print(df)
        #datata=list(df["wisata"])
        i=0
        for n in datata:
            if i==10:
                self.ulang()
            print(datata[0])
            print(i)
            self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/article/div[3]/section[3]/div/form/textarea").click()
            self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea").send_keys(tag,datata[0])
            self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/button").click()
            datata.pop(0)
            sleep(15)
            i=i+1
        self.ulang()
    
    def ulang(self):
        self.driver.get("https://instagram.com")
        sleep(random.randint(60,120))
        self.driver.get(post_link)
        sleep(random.randint(15,20))
        self.repeat()
            
            #self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[1]").click()
            #sleep(10)
            #self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()
            #sleep(40)
            #self.driver.get("https://www.instagram.com/p/CDsIgnpnYfV/")
            #sleep(20)
            
       
login(username,password)
