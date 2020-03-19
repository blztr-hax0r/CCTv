#Jangan ganti author , hargai creator cape loh buat nya

import BLZTR
from BLZTR.fr import *
from BLZTR.de import *
from BLZTR.id import *
from BLZTR.it import *
from BLZTR.jp import *
from BLZTR.kr import *
from BLZTR.tr import *
from BLZTR.us import *
import requests,re,os

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



def main():
    os.system('clear')
    print("        {}__  __         {}[~] {}Hack CCTV").format(cyan,y,r)
    print("      {} / / / /").format(cyan)
    print("  {} ___/ /_/ /___       {}[~] {}Script By : {}Blztr Hax0r").format(cyan,y,r,w)
    print("  {}/___  __  ___/").format(cyan)
    print("     {}/ / / /           {}[~] {}Youtube Channel : {}Zone Xploit").format(cyan,y,r,w)
    print("    {}/_/ /_/  ").format(cyan)
    print ("")
    print ("  {}[ 1 ] {}France").format(r,y)
    print ("  {}[ 2 ] {}Germany").format(r,y)
    print ("  {}[ 3 ] {}Indonesia").format(r,y)
    print ("  {}[ 4 ] {}Italy").format(r,y)
    print ("  {}[ 5 ] {}Japan").format(r,y)
    print ("  {}[ 6 ] {}Korea").format(r,y)
    print ("  {}[ 7 ] {}Turkey").format(r,y)
    print ("  {}[ 8 ] {}United States").format(r,y)
    print ("  {}[ 9 ] {}Exit").format(r,y)
    print ""
    select = input("\033[1;37m[ \033[1;36mBlztr\033[1;31m@\033[1;36mHax0r \033[1;37m]\033[1;34m ~\033[1;37m ")
    filtering(select)



def filtering(pilih):
    if pilih == 1:
        france()
    elif pilih == 2:
        german()
    elif pilih == 3:
        indonesia()
    elif pilih == 4:
        italy()
    elif pilih == 5:
        japan()
    elif pilih == 6:
        korea()
    elif pilih == 7:
        turkey()
    elif pilih == 8:
        unitedstates()
    elif pilih == 9:
        print (r+"Keluar ..."+w)
        os.sys.exit()
    else:
        print (r+"Keluar ..."+w)
        os.sys.exit()

if __name__ == '__main__':
    main()
