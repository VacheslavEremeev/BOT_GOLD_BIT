import requests
from bs4 import BeautifulSoup as BS

class ParseGold():
    def __init__(self, url):
        self.url = url
        self.values = []
        sourse = requests.get(self.url)
        self.html = BS(sourse.text, 'lxml')

    def get_content(self):
        table = self.html.find('table', {'class' : 'mfd-table'})
        thead = table.find('thead')            
        tbody = table.find('tbody')

        for tr in thead.find_all('tr'):
            th = tr.find_all('th', {'class':''})
            for value in th:
                if value.text != '':                   
                    self.values.append(value.text.replace('\r', '-'))


        for tr in tbody.find_all('tr'):
            td = tr.find_all('td', {'class':''})
            for value in td:
                if value.text != '':                   
                    self.values.append(value.text)       


        self.values = self.values[0:8]
        return self.values
        
########################################

class ParseUsd():
    def __init__(self, url):
        self.url = url
        self.values = []
        self.values1 = []
        sourse = requests.get(self.url)
        self.html = BS(sourse.text, 'lxml')

    def get_content_usd(self):
        div = self.html.find('div', {'class' : 'mfd-master-header-left'}) 
        text = div.get_text()
        text = text.replace('\xa0 ','\n')       
        textusd = text.rstrip()
     
        self.values = textusd

        return self.values         

##########################################

class ParseCrip():
    def __init__(self, url):
        self.url = url
        self.values = []
        sourse = requests.get(self.url)
        self.html = BS(sourse.text, 'lxml')

    def get_content_bit(self):
        table = self.html.find('table', {'class':'cmc-table cmc-table___11lFC cmc-table-homepage___2_guh'})
        tbody = table.find('tbody')
        spisok = []
        spisok22 = []

        for tr in tbody.find_all('tr'):
            td = tr.find_all('td', {'class':''})
            for value in td[2:4]:
                if value != '':
                    spisok.append(value.text)

        for i in spisok:
            if i == "Bitcoin1BTC" or i == "Ethereum2ETH" or i == "DogecoinDOGE" or i == "MoneroXMR":                   
                ind = spisok.index(i)
                nowin  = ind + 1
                spisok22.extend([spisok[ind], spisok[nowin]])
               
        self.values = spisok22
        return self.values   


class ParseSP500():
    def __init__(self, url):
        self.url = url
        self.values = []
        sourse = requests.get(self.url)
        self.html = BS(sourse.text, 'lxml')

    def get_content_sp(self):
        div = self.html.find('div', {'class':'pricebox content_box'})
        th = div.find_all('th', {'class':''})

        for value in th:
            if value.text != '':
                self.values.append(value.text.replace('\xa0', ''))

        return self.values
        print(self.values) 