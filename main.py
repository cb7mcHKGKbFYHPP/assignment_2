def remove_element(list_,index_):
        clipboard = []
        for i in range(len(list_)):
            if i is not index_:
                clipboard.append(list_[i])
        return clipboard


'''
АЛГОРИТМ
Програма зчитує інформацію з файлів та розбиває їх у списки list_of_countries
та list_of_results. Потім програма підраховує усі голоси, які країна отримала згідно
із заданою у завданні лоікою. Результат пакується в словник, і незвичайною командою
він сортується (де країни з найбільшою кількістю голосів знаходяться спочатку,
потім йдуть країни з меншою кількістю голосів), зберігаючи пари країна - сумарна кількість голосів. 
З нього залишається витягнути упорядковані країни у список та присвохїти їм оцінки із вже
заготованоо списку оцінок.

'''   
def estimate ():
    file = open("eurovision1.csv", "r")
    list_of_countries = file.read().splitlines()
    buffer_list = []
    list_of_results = []
    for line in list_of_countries:
        buffer_list = line.split(",")
        list_of_results.append(buffer_list)
        buffer_list = []
    list_of_results.pop(0)
    file.close()
    file = open("eurovision2.csv", "r")
    list_of_countries = file.read().splitlines()
    buffer_list = []
    for line in list_of_countries:
        buffer_list = line.split(",")
        list_of_results.append(buffer_list)
        buffer_list = []
    list_of_results.pop(10)
    print(list_of_results)
    file.close()
    countries = []
    votes = []
    for line in list_of_results:
        country = line[0]
        countries.append(country)
        sum_of_votes = 0
        for i in range(1, 20):
            sum_of_votes += int(line[i])
        votes.append(sum_of_votes)
        del sum_of_votes
    dictionary = dict(zip(countries, votes))
    marks = [12, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    sorted_dictionary = {keys: vals for keys, vals in sorted(dictionary.items(), key=lambda item: item[1])}
    marked_countries = sorted_dictionary.keys()
    to_write = dict(zip(marked_countries, marks))
    print(to_write)
    return to_write

def create_file():
    fout = open("output.txt", "w")
    fout.close()
    
def write(to_write):
    '''Функція, яка переписує в файл результат обчислень.'''
    fout = open("output.txt", "a")
    text1 = str(to_write)
    text2 = ""
    i = 1
    while text1:
        '''while не може самостійно зупинитися, тому
           використана "змушена" перевірка'''
        if text1[i] == text1[-1]:
          break
        text2 += text1[i]
        i += 1
    print(text2)
    fout.write(text2)
    del text1
    del text2
    fout.close()

create_file()
to_write = estimate()
write(to_write)

