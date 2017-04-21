import glob
import re

def Classificator (stroka):
    IP=re.match(' ip address (([0-9]{1,3}\.){3}[0-9]{1,3}) (([0-9]{1,3}\.){3}[0-9]{1,3})',stroka)
    INT=re.match('interface (.*)',stroka)
    HOST=re.match('hostname (.*)',stroka)
    if IP:
        IP=('IP',IP.group(1),IP.group(3))
        stroka=IP
    elif INT:
        INT=('INT',INT.group(1))
        stroka=INT
    elif HOST:
        HOST=('HOST',HOST.group(1))
        stroka=HOST
    else:
        stroka=('UNCLASSIFIED',)
    return(stroka)

list_of_files=glob.glob('C:\\work\\Python\\p4ne_training\\config_files\\*.txt')  #составляет список файлов с расширением .txt

for i in list_of_files:  #пробегаем по списку файлов
    with open (i) as f:  #открываем файл
        lines=f.readlines()  #формируем список строк файла
        for j in lines:  #пробегаем по строкам
            Str1=Classificator(j)
            if Str1[0]!='UNCLASSIFIED':
                print(Str1)


