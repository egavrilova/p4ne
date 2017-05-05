#импортируем библиотеки
import ipaddress
import random


#создаем класс
class IPv4RandomNetwork(ipaddress.IPv4Network):
    def __init__(self):
        ipaddress.IPv4Network.__init__(self,(random.randint(0x10000000,0xE0000000),random.randint(1,30)),strict=False)

# инициализируем пустой список
list1=[]

for i in range(1,10):
    list1.append(IPv4RandomNetwork())
#сортируем список
list1.sort()
print ('IP-networks sorted:')
for i in list1:
    print(i)
#создаем функцию, которая возвращает 64-битовое число, в котором маска занимает перввые 32 позиции
def Sortfunc(ipnet):
    return int(ipnet.network_address._ip) + int(ipnet.netmask._ip*2**32)
print('IP-networks sorted by mask:')

#Печатаем сортировку списка по ключу, использующему нашу функцию.
# Ссылаемся на функцию без передачи переменных, так как нас интересует не результат работы функции, а она используется как ключ.
for i in sorted(list1,key=Sortfunc):
    print(i)

