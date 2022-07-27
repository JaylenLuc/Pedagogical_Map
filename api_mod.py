import requests
import time
import json
import pandas as pd
import io
from bs4 import BeautifulSoup
from newsapi import NewsApiClient
import http.client, urllib.parse


newsapi = NewsApiClient(api_key='9d00f1ed20454836b2b1b30b5f84530a')

class server_fetch:
    fetch_time = 0
    response = ''
    news= ''
    hdi = ''
    def __init__(self):
        server_fetch.response = requests.get('https://restcountries.com/v3.1/all').json()
        #server_fetch.news = requests.get('https://newsapi.org/v2/everything?domains=aljazeera.com,apnews.com,reuters.com,cfr.org,foreignpolicy.com&apiKey=9d00f1ed20454836b2b1b30b5f84530a').json()
        server_fetch.hdi=pd.read_csv(io.StringIO(requests.get(BeautifulSoup(requests.get('https://hdr.undp.org/data-center/documentation-and-downloads').text,\
            'html.parser').find_all(text='HDI and components time-series')[0].parent['href']).content.decode('utf-8')))

    def get_news(self,iso2):

        conn = http.client.HTTPConnection('api.mediastack.com')

        params = urllib.parse.urlencode({
            'access_key': 'ACCESS_KEY',
            'categories': '-entertainment ,-health,-sports',
            'sort': 'published_desc',
            'limit': 5,
            'countries': str(iso2),
            })

        conn.request('GET', f'/v1/news?{params}')
        return conn.getresponse().read().decode('utf-8')



    def find_news(self):
        #server_fetch.news = requests.get('https://newsapi.org/v2/everything?domains=aljazeera.com,apnews.com,reuters.com,cfr.org,foreignpolicy.com&apiKey=9d00f1ed20454836b2b1b30b5f84530a').json()
        pass
        '''
        self.author = server_fetch.news['articles'][1]['author']
        self.title =server_fetch.news['articles'][1]['title']
        self.descr =server_fetch.news['articles'][1]['description']
        self.url =server_fetch.news['articles'][1]['url']
        self.img =server_fetch.news['articles'][1]['urlToImage']
        self.pub =server_fetch.news['articles'][1]['publishedAt']
        self.content = server_fetch.news['articles'][1]['content'][0:-14]
        pass
        '''
    @staticmethod 
    def rettime():
        return server_fetch.server_fetch.rettime
    def fetch(self,code):
        server_fetch.response = requests.get(f'https://restcountries.com/v3.1/alpha/{code}').json()
        return server_fetch.response[0]


    def fetch_assign(self,code):
        server_fetch.response = requests.get(f'https://restcountries.com/v3.1/alpha/{code}').json()
        self.native_name = f'Autochthonous Name: '+list(server_fetch.response[0]['name']['nativeName'].items())[0][1]['official'] #get native language name
        self.name = f'Anglophone Name: '+server_fetch.response[0]['name']['common'] #get name
        self.capital = f'Administrative Center: '+server_fetch.response[0]['capital'][0] #get capital
        self.subregion = f'Subregion: '+server_fetch.response[0]['subregion'] #get region
        self.lang = f'Lingua Franca: '+list(server_fetch.response[0]['languages'].items())[0][1] #get lang
        self.pop = f'Population: '+ str(server_fetch.response[0]['population']) #get pop
        self.time = f'Timezone (UTC): ' + server_fetch.response[0]['timezones'][0] #timezone
        try:
            self.gini = f'Gini Income Inequality Index: '+str(list(server_fetch.response[0]['gini'].values())[0])+ ' per ' + str(list(server_fetch.response[0]['gini'].keys())[0]) #gini index
        except(KeyError):
            self.gini = f'Gini Income Inequality Index: '+ 'N/A'
        
        try:
            self.money = f'Fiat Currency: '+ str(list(server_fetch.response[0]['currencies'].items())[0][1]['name'])+ ' '+ str(list(server_fetch.response[0]['currencies'].items())[0][1]['symbol']) #currrency #currencu symb

        except(KeyError):
            self.money = f'Fiat Currency: '+ str(list(server_fetch.response[0]['currencies'].items())[0][1]['name']) #currrency #currencu symb

    def raw_print(self,code):
        server_fetch.response = requests.get(f'https://restcountries.com/v3.1/alpha/{code}').json()
        print(server_fetch.response)
        
        #next order of business:: get the pop and try to do the images of flag
    def printer(self):
        print(self.native_name)
        print(self.name)
        print(self.capital)
        print(self.subregion)
        print(self.lang)
        print(self.pop)
        print(self.time)
        print(self.gini)
        print(self.money)


    
    def get_news_if(self,code):
        
        return requests.get(f'https://newsapi.org/v2/everything?q={code}domains=aljazeera.com,apnews.com,reuters.com,cfr.org,foreignpolicy.com&apiKey=9d00f1ed20454836b2b1b30b5f84530a').json()

    def form_str(self,code):
        #most  ofthe time is taken here

        start = time.time()
        #income = self.get_income(code)
        #response = requests.get(f'https://restcountries.com/v3.1/alpha/{code}').json()
        end = time.time()
        for i in range(250):
            #print(i)
            if server_fetch.response[i]['cca3'] == code:

                try:
                    color = ''
                    color_end = ''
                    style = ''
                    gin = float(list(server_fetch.response[i]['gini'].values())[0])
                    if gin < 30:
                        style = '<style>pr {color:#008000; display:inline;}</style> '
                        color = '<pr>'
                        color_end = '</pr>'
                    elif gin >= 30 and gin < 45:
                        style = '<style>pr {color:#FFA500; display:inline;}</style> '
                        color = '<pr>'
                        color_end = '</pr>'
                    elif gin >= 45 :
                        style = '<style>pr {color:#FF0000; display:inline;}</style> '
                        color = '<pr>'
                        color_end = '</pr>'
                    self.gini = style+ f'<b>Gini Income Inequality Index:</b> '+color+str(gin)+ color_end+' per ' + str(list(server_fetch.response[i]['gini'].keys())[0]) #gini index
                except(KeyError):
                    self.gini =style+ f'<b>Gini Income Inequality Index:</b> '+ 'N/A'
                
                try:
                    y = str(list(server_fetch.response[i]['currencies'].items())[0][1]['name'])
                    self.money = f'<b>Fiat Currency:</b> '+ y+ ' '+ str(list(server_fetch.response[i]['currencies'].items())[0][1]['symbol']) #currrency #currencu symb

                except(KeyError):
                    self.money = f'<b>Fiat Currency:</b> '+ y #currrency #currencu symb
                t = 0
                lang = ''
                name= ''

                for k,v in server_fetch.response[i]['languages'].items():
                    if t == 1: lang += '<b>Other languages:</b> '
                    if not t == 0: lang += f'{v} / '
                    t+= 1
                lang = lang[0:-2]
                if code == 'ZWE': name = list(server_fetch.response[i]['name']['nativeName'].items())[0][1]['official']
                else:

                    for k,v in server_fetch.response[i]['name']['nativeName'].items():
                        name += v['official'] + ' / '

                    name = name[0:-2]
                try:
                    income = income[1][0]['incomeLevel']['value']
                except:
                    income = 'N\A'
                try:
                    capital = server_fetch.response[i]['capital'][0]
                except(KeyError):
                    capital = 'N/A'

                year = int(BeautifulSoup(requests.get('https://hdr.undp.org/data-center/documentation-and-downloads').text,'html.parser').find_all(text='HDI and components time-series')[0].parent['href'][46:50]) - 1
                
                #print(code)
                 
                hdi_og = server_fetch.hdi[(server_fetch.hdi['iso3'] == f'{code}')]
                #print(hdi[f'hdi_rank_{year}'][:][1])
                if hdi_og.empty:
                    hdi = 'N/A'
                    ranked = 'N/A'
                    gni = 'N/A'
                    le = 'N/A'
                    mys = 'N/A'
                    eys = 'N/A'
                else:
                    hdi = [str(list(hdi_og[f'hdi_{year}'])[0]) if str(list(hdi_og[f'hdi_{year}'])[0]) != 'nan' else 'N/A'][0]
                    ranked = [str(list(hdi_og[f'hdi_rank_{year}'])[0])[0:-2] if str(list(hdi_og[f'hdi_rank_{year}'])[0])[0:-2] != 'nan' else 'N/A'][0]
                    gni = [str(list(hdi_og[f'gnipc_{year}'])[0]) if str(list(hdi_og[f'gnipc_{year}'])[0]) != 'nan' else 'N/A'][0]
                    le = [str(list(hdi_og[f'le_{year}'])[0]) if str(list(hdi_og[f'le_{year}'])[0]) != 'nan' else 'N/A'][0]
                    mys = [str(list(hdi_og[f'mys_{year}'])[0]) if str(list(hdi_og[f'mys_{year}'])[0]) != 'nan' else 'N/A'][0]
                    eys = [str(list(hdi_og[f'eys_{year}'])[0]) if str(list(hdi_og[f'eys_{year}'])[0]) != 'nan' else 'N/A'][0]
                    try: gni = float(gni)
                    except: pass
                #print(name)
                if not hdi_og.empty and hdi != 'N/A':
                    color = '<prh>'
                    color_end = '</prh>'
                    if float(hdi) >= .80: style = '<style>prh {color:#008000; display:inline;}</style> ' 
                    elif float(hdi) >= .7 and float(hdi) < .80: style = '<style>prh {color:#FFA500; display:inline;}</style> '  
                    elif float(hdi) >= .5 and float(hdi) < .7: style = '<style>prh {color:#FF5349; display:inline;}</style> '
                    elif float(hdi) < .5: style = '<style>prh {color:#FF0000; display:inline;}</style> '
                    hdi = style + color + hdi + color_end
                    ranked = style + color + ranked + color_end 
                if not hdi_og.empty and gni != 'N/A':
                    color = '<prg>'
                    color_end = '</prg>'
                    if float(gni) >= 13500: style = '<style>prg {color:#008000; display:inline;}</style> '
                    elif float(gni) >= 4500 and float(gni) < 13500: style = '<style>prg {color:#FFA500; display:inline;}</style> '
                    elif float(gni) >= 1200 and float(gni) < 4500: style = '<style>prg {color:#FF5349; display:inline;}</style> '
                    elif float(gni) < 1200: style = '<style>prg {color:#FF0000; display:inline;}</style> '
                    gni =  style + color + f'{gni:,}' + color_end
                if not hdi_og.empty and le != 'N/A':
                    color = '<prl>'
                    color_end = '</prl>'
                    if float(le) >= 80: style = '<style>prl {color:#008000; display:inline;}</style> '
                    elif float(le) >= 70 and float(le) < 80: style = '<style>prl {color:#FFA500; display:inline;}</style> '
                    elif float(le) >= 60 and float(le) < 70: style = '<style>prl {color:#FF5349; display:inline;}</style> '
                    elif float(le) < 60: style = '<style>prl {color:#FF0000; display:inline;}</style> '
                    le = style + color + str(le) + color_end
                if not hdi_og.empty and eys != 'N/A':
                    color = '<prey>'
                    color_end = '</prey>'
                    if float(eys) >= 14: style = '<style>prey {color:#008000; display:inline;}</style> '      
                    elif float(eys) >= 10 and float(eys) < 14: style = '<style>prey {color:#FFA500; display:inline;}</style> '
                    elif float(eys) < 10:style = '<style>prey {color:#FF0000; display:inline;}</style> '
                    eys = style + color + str(eys) + color_end
                if not hdi_og.empty and mys != 'N/A':
                    color = '<prm>'
                    color_end = '</prm>'
                    if float(mys) >= 12: style = '<style>prm {color:#008000; display:inline;}</style> '
                    elif float(mys) >= 8 and float(mys) < 12: style = '<style>prm {color:#FFA500; display:inline;}</style> '  
                    elif float(mys) < 8: style = '<style>prm {color:#FF0000; display:inline;}</style> '
                    mys = style + color + str(mys) + color_end
                if len(lang) != 0: lang += '</br>'
                #'<img src="data:image/jpeg;base64,{}">'
                #print(code)
                
                pop = server_fetch.response[i]['population']

                #print(pop)
                flag = server_fetch.response[i]['flags']['png']
                ret = f'<b>Autochthonous Name:</b> '+ name + '<br>'\
                        +f'<b>Anglophone Name:</b> '+server_fetch.response[i]['name']['common']+ '<br>'+f'<img src="{flag}" style="width:114px;height:60px;">'+'<br>'\
                            +str(f'<b>Administrative Center:</b> '+ capital) + '<br>'\
                                +str(f'<b>Subregion:</b> '+server_fetch.response[i]['subregion'])+ '<br>'\
                                    +  str( f'<b>Lingua Franca:</b> '+list(server_fetch.response[i]['languages'].items())[0][1])+ '<br>'\
                                        +lang + '<b>Population:</b> '+f'{pop:,}' + '<br>'\
                                                +str(f'<b>Timezone (UTC):</b> ' + server_fetch.response[i]['timezones'][0]) + '<br>'+self.gini + '<br>'+self.money + '<br>'\
                                                    +f'<b>Human Development Index ({year}):</b> '+hdi + '</br>'+\
                                                        '<b>HDI rank: </b>'+ranked+'<br>'+f'<b>Gross National Income Per Capita (PPP):</b> {gni}'+'<br>'+\
                                                            '<b>Life Expectancy at Birth:</b> '+ le+'<br>'+'<b>Expected Years of Schooling:</b> '+eys+'<br>'+\
                                                                '<b>Mean Years of Schooling:</b> '+ mys +'</div>'
                
                server_fetch.fetch_time += end-start
                break
            
        return ret




if __name__ == '__main__':
    y = server_fetch()
    print(y.raw_print('chn'))
    
