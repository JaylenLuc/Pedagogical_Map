import requests
import time
import json

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   

class server_fetch:
    fetch_time = 0
    response = ''

    def __init__(self):
        server_fetch.response = requests.get('https://restcountries.com/v3.1/all').json()
        #server_fetch.response = json.loads(server_fetch.response.read())

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


    
    def get_income(self,code):
        try:
            return requests.get(f'http://api.worldbank.org/v2/country/{code}?format=json').json()
        except:
            return 'N/A'

    def form_str(self,code):
        #most  ofthe time is taken here

        start = time.time()
        income = self.get_income(code)
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



                if len(lang) != 0: lang += '</br>'
                #'<img src="data:image/jpeg;base64,{}">'
                flag = server_fetch.response[i]['flags']['png']
                ret = f'<b>Autochthonous Name:</b> '+ name + '<br>'\
                        +f'<b>Anglophone Name:</b> '+server_fetch.response[i]['name']['common']+ '<br>'+f'<img src="{flag}" style="width:80px;height:60px;">'+'<br>'\
                            +str(f'<b>Administrative Center:</b> '+ capital) + '<br>'\
                                +str(f'<b>Subregion:</b> '+server_fetch.response[i]['subregion'])+ '<br>'\
                                    +  str( f'<b>Lingua Franca:</b> '+list(server_fetch.response[i]['languages'].items())[0][1])+ '<br>'\
                                        +lang + str(f'<b>Population:</b> '+ str(server_fetch.response[i]['population'])) + '<br>'\
                                                +str(f'<b>Timezone (UTC):</b> ' + server_fetch.response[i]['timezones'][0]) + '<br>'+self.gini + '<br>'+self.money + '<br>'\
                                                    +'<b>Income Level:</b> '+income +  '</div>'
                
                server_fetch.fetch_time += end-start
                break
            
        return ret




if __name__ == '__main__':
    y = server_fetch()
    print(y.raw_print('chn'))
    
