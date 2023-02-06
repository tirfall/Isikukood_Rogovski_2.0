
from calendar import month


def pikkus(ikood:str)->bool:
    if len(ikood)==11 and ikood.isdigit():
        flag=True
    else:
        flag=False
    return flag

def esimine(ikood:str)->str:
    
    ikood_list=list(map(int,ikood)) #[1,2,...]
    if ikood_list[0] in [1,3,5]:
        s="mees"
    elif ikood_list[0] in [2,4,6]:
        s="naine"
    else:
        s="viga"
    return s

def sunnipaev(ikood:str)->str:
    spaev=0
    ikood_list=list(ikood)
    y=ikood_list[1]+ikood_list[2]
    m=ikood_list[3]+ikood_list[4]
    d=ikood_list[5]+ikood_list[6]
    if int(d)>=1 and int(d)<=31 and int(m)>=1 and int(m)<=12:
        if int(ikood_list[0]) in [1,2]:
            yy="18"
        elif int(ikood_list[0]) in [3,4]:
            yy="19"
        else:
            yy="20"
        spaev=(f"{d}.{m}.{yy}{y}")
    else:
        print("Viga")
    return spaev
 

def sunnikoht(ikood: str)->str:
    ikood_list=list(ikood) 
    t=int(ikood_list[7]+ikood_list[8]+ikood_list[9])
    
    if t>=1 and t<=10:
        haigla="Kuressaare Haigla"
    elif t>=11 and t<=19:
        haigla="Taru Ülikooli NAistekliinik, Tartumaa, Tartu"
    elif t>=20 and t<=220:
        haigla="Ida-Tallinna Keskhaigla, Pelgulinna sünnitusmaja, Hiiumaa, Keila, Rapla haigla, Loksa haigla"
    elif t>=221 and t<=270:
        haigla=" Ida-Viru Keskhaigla (Kohtla-Järve, endine Jõhvi)"
    elif t>=271 and t<=370:
        haigla="Maarjamõisa Kliinikum (Tartu), Jõgeva Haigla"
    elif t>=371 and t<=420:
        haigla="Narva Haigla"
    elif t>=421 and t<=470:
        haigla="Pärnu Haigla"
    elif t>=471 and t<=490:
        haigla="Pelgulinna Sünnitusmaja (Tallinn), Haapsalu haigla"
    elif t>=491 and t<=520:
        haigla="Järvamaa Haigla (Paide)"
    elif t>=521 and t<=570:
        haigla="Rakvere, Tapa haigla"
    elif t>=571 and t<=600:
        haigla="Valga Haigla"
    elif t>=601 and t<=650:
        haigla="Viljandi Haigla"
    elif t>=651 and t<=700:
        haigla<="Lõuna-Eesti Haigla (Võru), Põlva Haigla"
    else:
        haigla="Välismaal"
    return haigla



def lause(ikood)->str:
    print(f"See on {esimine(ikood)} ta on sündinud {sunnipaev(ikood)}, tema sünnikoht on {sunnikoht(ikood)}")
