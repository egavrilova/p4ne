import sys
import glob
from flask import Flask, jsonify

app = Flask(__name__)
@app.route('/')
@app.route('/index')
def index():
 return "Привет!" \
        "<br>Если хотите вывести справку по Питону, обратитесь к странице " \
        "<a href='http://localhost:5000/python'>/python</a>" \
        "<br>Если хотите посмотреть, для каких устройств у нас есть конфигурационные файлы, обратитесь к странице " \
        "<a href='http://localhost:5000/configs'>/configs</a>" \
        "<br>Если хотите вывести информацию о IP-адресах конкретного устройства, смотрите страницу /configs/hostname" \
        "<br>(вместо 'hostname' введите имя устройтства)"
@app.route('/python')
def python():
    return jsonify(repr(sys.__dict__))
@app.route('/configs')
def configs():
    return jsonify(No_dubl)
@app.route('/configs/<hostname>')
def f(hostname):
    return jsonify(Mega_dict[hostname])

if __name__ == '__main__':
    list_of_files = glob.glob(
        'C:\\work\\Python\\p4ne_training\\config_files\\*.txt')  # составляет список файлов с расширением .txt
    Mega_list = []
    Mega_dict = {}
    for i in list_of_files:
        with open(i) as f:
            lines = f.readlines()
            for j in lines:
                str_num1 = j.find('hostname')
                str_num2 = j.find('ip address')
                if str_num1 == 0:
                    j1 = j.replace('hostname', '').strip()
                    Mega_list.append(j1)
                    Mega_dict[j1]=[]
                if str_num2 == 1:
                    j2 = j.replace('ip address', '').strip()
                    Mega_dict[j1].append(j2)
    No_dubl = list(set(Mega_list))
    app.run(debug=True)
