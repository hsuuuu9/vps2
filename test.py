import urllib.request as request
import datetime
import json


API = "http://api.aoikujira.com/kawase/get.php?code=USD&format=json"
json_str = 'mede'
print("1USD")


t = datetime.datetime.now()
fname = "aa.json"
with open(fname, "w", encoding="utf-8") as f:
    f.write(str(t.strftime('%Y-%m-%d %H:%M:%S')))
