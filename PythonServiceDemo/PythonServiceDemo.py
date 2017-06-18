## 8ea7cc4a9190f6c67ddb71d65560379e
import json
import urllib.parse
import urllib.request

url = 'https://test.fizbot.net/properties?ownership=own&page=1&limit=5&status=&text=&min_price=&max_price=&property_stats=1&currency=1'

token = '8ea7cc4a9190f6c67ddb71d65560379e'
#headers = {'x-es-api-token': token}
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"}
#data = urllib.parse.urlencode(headers)
#data = data.encode('utf-8')
request = urllib.request.Request(url, headers = headers)
request.add_header('x-es-api-token', token)

 #  the_page = response.read()

 # print(the_page)
  
response = urllib.request.urlopen(request).read()


jsonValue = json.loads(response)
propertiesArray = jsonValue['PropertiesResponse']['Properties']

for property in propertiesArray:
	print(property['District']['name'])

    #