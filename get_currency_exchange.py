import json
import requests
from bs4 import BeautifulSoup as bs

def find_between(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ""

def build_req(method, url, headers, data=None):
     req = requests.Request(method, url, headers=headers, data=data)
     req = req.prepare()
     s = requests.Session()
     r = s.send(req, verify=False)
     r.close
     return r

def fetch_currency_exchange_rates(host):
    response = requests.get(host)

    if response.status_code != 200:
        raise Exception('Unexpected GET Result: {} {}'.format(response.status_code, response.text))

    soup = bs(response.text.encode("utf-8"), "html.parser")
    tds = soup.find_all('td', {'class': 'rtRates'})
    currencies = {}

    for td in tds:
        src = find_between(td.a['href'], "from=", "&")
        trg = td.a['href'].split('to=')[-1]
        if src == "USD" and trg.strip() and td.text.strip():
            currencies[trg.strip()] = td.text.strip()

    return currencies

if __name__ == '__main__':
    host = 'https://www.x-rates.com/table/?from=USD&amount=1'
    currencies = fetch_currency_exchange_rates(host)
    print(currencies)

    #host = 'https://www.host.com'
    #headers = {'Content-Type':'application/json'}
    #payload = {'firstName': 'sample', 'lastName': 'random'}
    #response = product_req('POST', host, headers=headers, data=payload)
    #response = product_req('GET', host, headers=headers)
    #auth = ('username', 'password')
    #response = requests.patch(host, auth=auth, headers=headers, data=json.dumps(payload))
    #if response.status_code != 200:
    #     raise Exception('Unexpected GET Result: {} {}'.format(response.status_code, response.text))
    #parsed = json.loads(response.text)
    #print(json.dumps(parsed, indent=2, sort_keys=True))
