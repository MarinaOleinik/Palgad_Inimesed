import random
log_list=[]
pas_list=[]
def login():
    pass
def auto_reg():
    """Salasõna genireerimine

    Tagastab salasõna str formaadis 

    :rtype: str
    """
    str0=".,:;!_*-+()/#¤%&"
    str1 = '0123456789'
    str2 = 'qwertyuiopasdfghjklzxcvbnm'
    str3 = str2.upper()
    str4 = str0+str1+str2+str3
    ls = list(str4)
    random.shuffle(ls)
    pas = ''.join([random.choice(ls) for x in range(12)])
    return pas 
def ise_reg():
    pass
def avtor():
    return a
def reg(v: str,l: list, p: list):
    """Inimese registreerimine

    Tagastab loginide ja salasõnade listid 

    :param str v: kasutaja parooli loomise viis
    :rtype: list,list
    """
    login()
    if v=="a":
        pas=auto_reg()
    else:
        ise_reg()
    return l,p
while 1:
    print("Registreerimine, autoriseerimine või välja")
    v=input("Sinu valik:")
    if v=="r":
        reg(input("Auto või ise?"),)
    elif v=="a":
        t=avtor()# True , False
        if avtor():
            print("Tere tulemast!")
        else:
            v=input("Kas tahed registreerida?")
            if v=="jah":
                print("Registreerimine")

            else:
                pass
    else:
        break
