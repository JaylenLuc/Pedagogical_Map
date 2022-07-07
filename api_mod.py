import requests

def fetch():
    response = requests.get(r'https://restcountries.com/v3.1/all').json()
    print(response)








if __name__ == 'main':
    fetch()
