# coding=utf-8

import csv
import numpy as np
from bs4 import BeautifulSoup
import requests
import codecs

# -*- coding: UTF-8 -*-
Division = {"牙科":"https://sp1.hso.mohw.gov.tw/doctor/All/history.php?UrlClass=%A4%FA%AC%EC&SortBy=q_no&PageNo=1", \
"外科":"https://sp1.hso.mohw.gov.tw/doctor/All/history.php?UrlClass=%A5~%AC%EC&SortBy=q_no&PageNo=1", \
"兒科":"https://sp1.hso.mohw.gov.tw/doctor/All/history.php?UrlClass=%A8%E0%AC%EC&SortBy=q_no&PageNo=1", \
"骨科":"https://sp1.hso.mohw.gov.tw/doctor/All/history.php?UrlClass=%B0%A9%AC%EC&SortBy=q_no&PageNo=1", \
"眼科":"https://sp1.hso.mohw.gov.tw/doctor/All/history.php?UrlClass=%B2%B4%AC%EC&SortBy=q_no&PageNo=1", \
"中醫科":"https://sp1.hso.mohw.gov.tw/doctor/All/history.php?UrlClass=%A4%A4%C2%E5%AC%EC&SortBy=q_no&PageNo=1", \
"皮膚科":"https://sp1.hso.mohw.gov.tw/doctor/All/history.php?UrlClass=%A5%D6%BD%A7%AC%EC&SortBy=q_no&PageNo=1", \
"泌尿科":"https://sp1.hso.mohw.gov.tw/doctor/All/history.php?UrlClass=%AAc%A7%BF%AC%EC&SortBy=q_no&PageNo=1", \
"家醫科":"https://sp1.hso.mohw.gov.tw/doctor/All/history.php?UrlClass=%AEa%C2%E5%AC%EC&SortBy=q_no&PageNo=1", \
"高年科":"https://sp1.hso.mohw.gov.tw/doctor/All/history.php?UrlClass=%B0%AA%A6~%AC%EC&SortBy=q_no&PageNo=1", \
"婦產科":"https://sp1.hso.mohw.gov.tw/doctor/All/history.php?UrlClass=%B0%FC%B2%A3%AC%EC&SortBy=q_no&PageNo=1", \
"麻醉科":"https://sp1.hso.mohw.gov.tw/doctor/All/history.php?UrlClass=%B3%C2%BEK%AC%EC&SortBy=q_no&PageNo=1", \
"復健科":"https://sp1.hso.mohw.gov.tw/doctor/All/history.php?UrlClass=%B4_%B0%B7%AC%EC&SortBy=q_no&PageNo=1", \
"腫瘤科":"https://sp1.hso.mohw.gov.tw/doctor/All/history.php?UrlClass=%B8~%BDF%AC%EC&SortBy=q_no&PageNo=1", \
"精神科":"https://sp1.hso.mohw.gov.tw/doctor/All/history.php?UrlClass=%BA%EB%AF%AB%AC%EC&SortBy=q_no&PageNo=1", \
"耳鼻喉科":"https://sp1.hso.mohw.gov.tw/doctor/All/history.php?UrlClass=%A6%D5%BB%F3%B3%EF%AC%EC&SortBy=q_no&PageNo=1", \
"放射線科":"https://sp1.hso.mohw.gov.tw/doctor/All/history.php?UrlClass=%A9%F1%AEg%BDu%AC%EC&SortBy=q_no&PageNo=1", \
"神經內科":"https://sp1.hso.mohw.gov.tw/doctor/All/history.php?UrlClass=%AF%AB%B8g%A4%BA%AC%EC&SortBy=q_no&PageNo=1", \
"神經外科":"https://sp1.hso.mohw.gov.tw/doctor/All/history.php?UrlClass=%AF%AB%B8g%A5~%AC%EC&SortBy=q_no&PageNo=1", \
"胸腔內科":"https://sp1.hso.mohw.gov.tw/doctor/All/history.php?UrlClass=%AF%DD%B5%C4%A4%BA%AC%EC&SortBy=q_no&PageNo=1", \
"整型外科":"https://sp1.hso.mohw.gov.tw/doctor/All/history.php?UrlClass=%BE%E3%AB%AC%A5~%AC%EC&SortBy=q_no&PageNo=1", \
"肝膽腸胃科":"https://sp1.hso.mohw.gov.tw/doctor/All/history.php?UrlClass=%A8x%C1x%B8z%ADG%AC%EC&SortBy=q_no&PageNo=1", \
"心臟血管專科":"https://sp1.hso.mohw.gov.tw/doctor/All/history.php?UrlClass=%A4%DF%C5%A6%A6%E5%BA%DE%B1M%AC%EC&SortBy=q_no&PageNo=1", \
"乳房甲狀腺科":"https://sp1.hso.mohw.gov.tw/doctor/All/history.php?UrlClass=%A8%C5%A9%D0%A5%D2%AA%AC%B8%A2%AC%EC&SortBy=q_no&PageNo=1"}



class Crawler:

    def __init__(self):
    
        pass
        
    def getAllArticles(self,division):
        
        i =0
        
        link = Division[division]
        
        f = codecs.open(division+'.csv', 'w', 'utf_8_sig')
        
        writer = csv.writer(f)
        
        while (link):
        
            i+=1
            
            print ("page ",i)
            
            urls = self.getUrl(link)
        
            for url in urls:
                writer.writerow(self.getQandA(url))
                
            link = self.getNextPage(link)
        
        f.close()
        
    def getNextPage(self,link):
    
        response = requests.get(url=link)
        
        response.encoding = 'big5'
        
        page = response.text
        
        soup = BeautifulSoup(page, 'html.parser')
        
        item = soup.find('a',attrs={'accesskey':'3'})
        
        next=None
        
        if item :
            next =  item.get('href')
        
        if next :
            next = 'https://sp1.hso.mohw.gov.tw/doctor/All/' + next
        
        return next
    
    def getUrl(self,table):
    
        response = requests.get(url=table)
        
        response.encoding = 'big5'
        
        page = response.text
        
        soup = BeautifulSoup(page, 'html.parser')
        
        urls = []
        
        soup = soup.find('table', attrs={'class': 'table1'})
        
        for link in  soup.find_all('a'):
        
            urls.append( 'https://sp1.hso.mohw.gov.tw/doctor/All/'+link.get('href') )
            
        return urls
    
    def getQandA(self,url):
        
        response = requests.get(url=url)
        
        response.encoding = 'big5'
        
        page = response.text

        soup = BeautifulSoup(page, 'html.parser')
        
        output = []
        
        output.append( soup.find('li', attrs={'class': 'subject'}).text )
        
        output.append( soup.find('li', attrs={'class': 'asker'}).text )
        
        output.append( soup.find('li', attrs={'class': 'ask'}).text )
        
        output.append( soup.find('li', attrs={'class': 'doctor'}).text )
        
        output.append( soup.find('li', attrs={'class': 'ans'}).text )
        
        return output
        

def main():

    crawler = Crawler()
    
    x=crawler.getAllArticles("復健科")

if __name__ =='__main__':

    main()
    
