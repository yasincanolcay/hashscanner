#code=utf-8

import requests
from time import sleep
from bs4 import BeautifulSoup


banner = """ 
██╗  ██╗ █████╗ ███████╗██╗  ██╗    ███████╗ ██████╗ █████╗ ███╗   ██╗
██║  ██║██╔══██╗██╔════╝██║  ██║    ██╔════╝██╔════╝██╔══██╗████╗  ██║
███████║███████║███████╗███████║    ███████╗██║     ███████║██╔██╗ ██║
██╔══██║██╔══██║╚════██║██╔══██║    ╚════██║██║     ██╔══██║██║╚██╗██║
██║  ██║██║  ██║███████║██║  ██║    ███████║╚██████╗██║  ██║██║ ╚████║
╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝    ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝                                                                     
"""
print(banner)
print("[md5-sha1]")
print("---------------------------------------------------------------")
print("[+]LÜTFEN FORMAT GİRİNİZ")
print("---------------------------------------------------------------")
format = input(">>>[+]BİR FORMAT SEÇİNİZ / [MD5]-[SHA1]: ")
print("\n")
if format == "md5" or format == "MD5":
    print("---------------------------------------------------------------")
    print("[+]LÜTFEN HASH GİRİNİZ")
    print("---------------------------------------------------------------")
    md5 = input(">>>[+]HASH: ")
    print("\n")
    sorgula = "https://md5.gromweb.com/?md5={}".format(md5)
    istek_yolla = requests.get(sorgula)
    sleep(3)
    soup = BeautifulSoup(istek_yolla.content,"lxml")
    hash_bilgisi = soup.find_all("em",attrs={"class":"long-content string"})

    for hash in hash_bilgisi:

        print("[+]search hash: {}".format(md5),"\n")
        print("---------------------------------")
        print("[%]HASH: {}".format(hash.text))
        print("---------------------------------")
#-------------------------------------
elif format == "sha1" or format == "SHA1":

    print("---------------------------------------------------------------")
    print("[+]LÜTFEN HASH GİRİNİZ")
    print("---------------------------------------------------------------")
    sha = input(">>>[+]HASH: ")
    print("\n")
    sorgula = "https://sha1.gromweb.com/?hash={}".format(sha)
    istek_yolla = requests.get(sorgula)
    sleep(3)
    soup = BeautifulSoup(istek_yolla.content,"lxml")
    hash_bilgisi = soup.find_all("em",attrs={"class":"long-content string"})

    for hash in hash_bilgisi:

        print("[+]search hash: {}".format(sha),"\n")
        print("---------------------------------")
        print("[%]HASH: {}".format(hash.text))
        print("---------------------------------")

else:

    print("[LÜTFEN GEÇERLİ BİR SEÇİM YAPINIZ]")


input()
