import glob
list_of_files=glob.glob('C:\\work\\Python\\p4ne_training\\config_files\\*.txt')  #составляет список файлов с расширением .txt
Mega_list=[]  #создаем пустой список
for i in list_of_files:  #пробегаем по списку файлов
    with open (i) as f:  #открываем файл
        lines=f.readlines()  #формируем список строк файла
        for j in lines:  #пробегаем по строкам
            str_num=j.find('ip address')  #вычисляем позицию подстроки в строке
            if str_num==1:  #все строки содержащие подстроку ip address в конфигурации списка начинаются с пробела, поэтому нас интересует позиция номер 1
                j=j.replace('ip address','').strip()  #убираем лишние пробелы и слова
                Mega_list.append(j)  #добавляем строку в мега-лист
No_dubl=list(set(Mega_list))  #удаляем дублирующиеся строки (это происходит при превращении списка в множество)
for i in No_dubl:
    print(i)


print (No_dubl)

