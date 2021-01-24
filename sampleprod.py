import json
import requests

def product_req(method, url, headers, data=None):
     req = requests.Request(method, url, headers=headers, data=data)
     req = req.prepare()
     s = requests.Session()
     r = s.send(req, verify=False)
     r.close
     return r

tenantId = 'mav-qa-int'
oAuthTokenUrl = 'https://' + tenantId + '.authentication.us10.hana.ondemand.com/oauth/token'
oAuthTokenHeader = {'Content-Type':'application/x-www-form-urlencoded'}
oAuthTokenPayload = {'grant_type': 'client_credentials', 'client_id': 'sb-caas2-xsuaa!t656', 'client_secret': 'hNYCN61kDkYBmHFb7e3waKgnohY='}
oAuthTokenResponse = product_req('POST', oAuthTokenUrl, headers=oAuthTokenHeader, data=oAuthTokenPayload)

print(oAuthTokenResponse.status_code)
print(oAuthTokenResponse.json().get("access_token"))

accessToken = oAuthTokenResponse.json().get("access_token")
headers = {'Accept-Language':'en-US', 'User-Agent':'Test/1.0', 'Accept':'application/json', 'Authorization':'Bearer ' + accessToken}
host = 'https://product-content-caas2-sap-test.cfapps.us10.hana.ondemand.com'

# Luckily we do not need pagination since there are less than 50 presets
response = product_req('GET', host + '/sellingtrees/0d5d2155-0a51-45dc-9057-92c66c12f871/products?types=PARENT%2CREGULAR%2CCOLLECTION&categoryIds=&expand=variantSummary&pageNumber=4&editionId=d59db052-4527-47d7-aae5-f21fc64321b4&pageSize=20&active=true&published=true&categoryIdsMode=PATH', headers=headers)
parsed = json.loads(response.text)
print(json.dumps(parsed, indent=2, sort_keys=True))
if response.status_code != 200:
     raise Exception('Unexpected GET Result: {} {}'.format(response.status_code, response.text))
