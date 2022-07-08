import requests
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

    def fetch(self,code):
        response = requests.get(f'https://restcountries.com/v3.1/alpha/{code}').json()
        return response[0]


    def fetch_assign(self,code):
        response = requests.get(f'https://restcountries.com/v3.1/alpha/{code}').json()
        self.native_name = f'Autochthonous Name: '+list(response[0]['name']['nativeName'].items())[0][1]['official'] #get native language name
        self.name = f'Anglophone Name: '+response[0]['name']['common'] #get name
        self.capital = f'Administrative Center: '+response[0]['capital'][0] #get capital
        self.subregion = f'Subregion: '+response[0]['subregion'] #get region
        self.lang = f'Lingua Franca: '+list(response[0]['languages'].items())[0][1] #get lang
        self.pop = f'Population: '+ str(response[0]['population']) #get pop
        self.time = f'Timezone (UTC): ' + response[0]['timezones'][0] #timezone
        try:
            self.gini = f'Gini Income Inequality Index: '+str(list(response[0]['gini'].values())[0])+ ' per ' + str(list(response[0]['gini'].keys())[0]) #gini index
        except(KeyError):
            self.gini = f'Gini Income Inequality Index: '+ 'N/A'
        
        try:
            self.money = f'Fiat Currency: '+ str(list(response[0]['currencies'].items())[0][1]['name'])+ ' '+ str(list(response[0]['currencies'].items())[0][1]['symbol']) #currrency #currencu symb

        except(KeyError):
            self.money = f'Fiat Currency: '+ str(list(response[0]['currencies'].items())[0][1]['name']) #currrency #currencu symb

    def raw_print(self,code):
        response = requests.get(f'https://restcountries.com/v3.1/alpha/{code}').json()
        print(response)
        
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


    def in_fetch(self):
        self.income  = requests.get('http://api.worldbank.org/v2/country?format=json').json()
    
    def form_str(self,code):
        income = requests.get(f'http://api.worldbank.org/v2/country/{code}?format=json').json()
        response = requests.get(f'https://restcountries.com/v3.1/alpha/{code}').json()
        try:
            color = ''
            color_end = ''
            style = ''
            if int(list(response[0]['gini'].values())[0]) < 30:
                style = '<style>pr {color:#008000; display:inline;}</style> '
                color = '<pr>'
                color_end = '</pr>'
            elif int(list(response[0]['gini'].values())[0]) >= 30 and int(list(response[0]['gini'].values())[0]) < 45:
                style = '<style>pr {color:#FFA500; display:inline;}</style> '
                color = '<pr>'
                color_end = '</pr>'
            elif int(list(response[0]['gini'].values())[0]) >= 45 :
                style = '<style>pr {color:#FF0000; display:inline;}</style> '
                color = '<pr>'
                color_end = '</pr>'
            self.gini = style+ f'<b>Gini Income Inequality Index:</b> '+color+str(list(response[0]['gini'].values())[0])+ color_end+' per ' + str(list(response[0]['gini'].keys())[0]) #gini index
        except(KeyError):
            self.gini =style+ f'<b>Gini Income Inequality Index:</b> '+ 'N/A'
        
        try:
            self.money = f'<b>Fiat Currency:</b> '+ str(list(response[0]['currencies'].items())[0][1]['name'])+ ' '+ str(list(response[0]['currencies'].items())[0][1]['symbol']) #currrency #currencu symb

        except(KeyError):
            self.money = f'<b>Fiat Currency:</b> '+ str(list(response[0]['currencies'].items())[0][1]['name']) #currrency #currencu symb
        t = 0
        lang = ''
        name= ''

        for k,v in response[0]['languages'].items():
            if t == 1: lang += '<b>Other languages:</b> '
            if not t == 0: lang += f'{v} / '
            t+= 1
        lang = lang[0:-2]
        if code == 'ZWE': name = list(response[0]['name']['nativeName'].items())[0][1]['official']
        else:

            for k,v in response[0]['name']['nativeName'].items():
                name += v['official'] + ' / '

            name = name[0:-2]
        try:
            income = income[1][0]['incomeLevel']['value']
        except:
            income = 'N\A'
        if len(lang) != 0: lang += '</br>'
        return f'<b>Autochthonous Name:</b> '+ name + '<br>'\
                +f'<b>Anglophone Name:</b> '+response[0]['name']['common']+ '<br>'\
                    +str(f'<b>Administrative Center:</b> '+response[0]['capital'][0]) + '<br>'\
                        +str(f'<b>Subregion:</b> '+response[0]['subregion'])+ '<br>'\
                            +  str( f'<b>Lingua Franca:</b> '+list(response[0]['languages'].items())[0][1])+ '<br>'\
                                +lang + str(f'<b>Population:</b> '+ str(response[0]['population'])) + '<br>'\
                                        +str(f'<b>Timezone (UTC):</b> ' + response[0]['timezones'][0]) + '<br>'+self.gini + '<br>'+self.money + '<br>'\
                                            +'<b>Income Level:</b> '+income +  '</div>'



if __name__ == '__main__':
    y = server_fetch()
    print(y.fetch('chn'))
    
