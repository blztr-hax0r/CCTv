#Jangan ganti author , hargai creator cape loh buat nya

import requests,os,re

b="\033[0;34m"
g="\033[1;32m"
w="\033[1;37m"
r="\033[1;31m"
y="\033[1;33m"
cyan = "\033[1;36m"
lgray = "\033[0;37m"
dgray = "\033[1;30m"
ir = "\033[0;101m"
reset = "\033[0m"


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}



def korea():
    global page
    res = requests.get('https://www.insecam.org/en/bycountry/KR/', headers=headers)
    findpage = re.findall('"?page=",\s\d+', res.text)[1]
    rfindpage = findpage.replace('page=", ', '')
    os.system('clear')
    print("        {}__  __         {}[~] {}Hack CCTV {}Korean").format(cyan,y,r,y)
    print("      {} / / / /").format(cyan)
    print("  {} ___/ /_/ /___       {}[~] {}Script By : {}Blztr Hax0r").format(cyan,y,r,w)
    print("  {}/___  __  ___/").format(cyan)
    print("     {}/ / / /           {}[~] {}Youtube Channel : {}Zone Xploit").format(cyan,y,r,w)
    print("    {}/_/ /_/  ").format(cyan)
    print ("")
    print("{}       [ {}Daftar Halaman : {} {}]").format(r,cyan,rfindpage,r)
    run()
    
def run():
    try:
        page = input("\033[1;31m       [ \033[1;36mHalaman \033[1;31m]\033[1;34m ~\033[1;33m ")
        url = ("https://www.insecam.org/en/bycountry/KR/?page="+str(page))
        print ""
        res = requests.get(url, headers=headers)
        findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
        count = 1
        for _ in findip:
             hasil = findip[count]
             print ("{}[ {}{} {}]").format(r,cyan,hasil,r)
             count += 1
    except:
        print ""
        print r+"Makasi udh pake tools kami"+w
