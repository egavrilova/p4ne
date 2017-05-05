import glob
import ipaddress
import re

Mega_set=set()
IP_set=set()  #множество всех кортежей (Сеть/Маска, IPaddr)
GW_set=set()  #множество кортежей (GW_Addr, "команда")
Net_set=set()  #множество сетей
def Classify (stroka):
    IP=re.match(' ip address (([0-9]{1,3}\.){3}[0-9]{1,3}) (([0-9]{1,3}\.){3}[0-9]{1,3})',stroka)
    if IP:
        IP_set.add((ipaddress.IPv4Network((IP.group(1), IP.group(3)), strict=False),IP.group(1)))
        return
    GW=re.match('ip default-gateway (.*)',stroka)
    if GW:
        GW_set.add((ipaddress.IPv4Address(GW.group(1)),'ip default-gateway command'))
        return
    NH=re.match('ip route 0.0.0.0 0.0.0.0 (.*)',stroka)
    if NH:
        GW_set.add((ipaddress.IPv4Address(NH.group(1)),'ip route command'))
        return
    VRRP=re.match(' vrrp (.+) ip (.*)',stroka)
    if VRRP:
        GW_set.add((ipaddress.IPv4Address(VRRP.group(2)),'vrrp command'))
        return
    GLBP = re.match(' glbp (.+) ip (.*)', stroka)
    if GLBP:
        GW_set.add((ipaddress.IPv4Address(GLBP.group(2)),'glbp command'))
        return
    HSRP = re.match(' standby (.+) ip (.*)', stroka)
    if HSRP:
        GW_set.add((ipaddress.IPv4Address(HSRP.group(2)),'standby command'))
        return

list_of_files=glob.glob('C:\\work\\Python\\p4ne_training\\config_files\\*.txt')  #составляет список файлов с расширением .txt
for i in list_of_files:  #пробегаем по списку файлов
    with open (i) as f:  #открываем файл
        lines=f.readlines()  #формируем список строк файла
        for j in lines:  #пробегаем по строкам
            Classify(j)

for gateway in GW_set:
   for net_mask_gw in IP_set:
       if gateway[0] in net_mask_gw[0]:
        Mega_set.add((net_mask_gw[0],gateway[0],gateway[1]))  #формируем итоговое множество кортежей
        Net_set.add(net_mask_gw[0])  #формируем множество сетей, для которых известен шлюз
for net_mask_gw in IP_set:
    if not(net_mask_gw[0] in Net_set):
        Mega_set.add((net_mask_gw[0],net_mask_gw[1],'Inter-router Link or stub network'))
def Sortfunc(ipnet):
    return int(ipnet[0].network_address._ip)
Megalist=list(Mega_set)
print('Network/Mask, Gateway, Description')
for i in sorted(Megalist,key=Sortfunc):
    print(i[0],i[1],i[2])

