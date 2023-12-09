import urllib.request
import json

url = "http://openapi.seoul.go.kr:8088/5a6e69665a64646f353578416e4359/json/TbPublicWifiInfo/1/500"
response = urllib.request.urlopen(url)
json_str = response.read().decode("utf-8")
data = json.loads(json_str)
print(json.dumps(data, indent=4, ensure_ascii=False))
