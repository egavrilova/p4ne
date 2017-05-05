import requests, json, pprint
from flask import Flask, jsonify, render_template

def new_ticket():
   url = 'https://sandboxapic.cisco.com/api/v1/ticket'
   payload = {"username": "devnetuser",
                "password": "Cisco123!"
              }
   header = {"content-type": "application/json"}
   response = requests.post(url, data=json.dumps(payload),headers=header, verify=False)
   return response.json()['response']['serviceTicket']


app = Flask(__name__)
@app.route('/')
def index():
    return render_template('topology.html')
@app.route('/api/topology')
def f():
    return jsonify(response3.json()['response'])

if __name__ == '__main__':
    ticket = new_ticket()
    controller = "devnetapi.cisco.com/sandbox/apic_em"
    url1 = "https://" + controller + "/api/v1/host"
    url2 = "https://" + controller + "/api/v1/network-device"
    url3 = "https://" + controller + "/api/v1/topology/physical-topology"
    header = {"content-type": "application/json", "X-Auth-Token":ticket
              }
    response1 = requests.get(url1, headers=header, verify=False)
    response2 = requests.get(url2, headers=header, verify=False)
    response3 = requests.get(url3, headers=header, verify=False)
    print("Hosts = ")
    pprint.pprint(response1.json())
    print("Network Devices = ")
    pprint.pprint(response2.json())
    print("Topology = ")
    pprint.pprint(response3.json())
    app.run(debug=True)