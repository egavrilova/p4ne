import sys, requests, pprint,argparse

http_proxy = 'http://193.203.100.139:8080'
https_proxy = 'https://193.203.100.139:8080'
proxyDict = {
            'http' : http_proxy,
            'https' : https_proxy
            }

r = requests.get('https://lookup.binlist.net/63930000', headers={'Accept-Version': '3'}, proxies=proxyDict)
print (r.status_code)
if 200 <= r.status_code < 299:
    pprint.pprint(r.json())

parser = argparse.ArgumentParser()
parser.add_argument('list', nargs="*")
args = parser.parse_args()

for i in args.list:
    r = requests.get('https://lookup.binlist.net/' + i, headers={'Accept-Version': '3'}, proxies=proxyDict)
    print(r.status_code)
    if 200 <= r.status_code < 299:
        pprint.pprint(r.json()['bank']['name'])



