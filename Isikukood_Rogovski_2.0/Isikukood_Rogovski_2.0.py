from xmlrpc.client import DateTime
from oma_moodul2 import *
ikood=""
while True:
    ikood=input("Sisesta isikukood: ")
    if pikkus(ikood)==False:
        print("Liiga pikk või lühike isikukood")
    else:
        s = esimine (ikood)
        if s=="viga":
            print("Esimene täht ei ole õige")
        else:
            if sunnipaev(ikood)=="viga":
                print("2-7 tähed on valesti sisestatud")
            else:
                lause(ikood)





