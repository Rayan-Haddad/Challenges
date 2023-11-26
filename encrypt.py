# encrypting messages 
def verif(x: str):
    for i in x:
        if i.islower() != True:
            return False
        return True

def esp(x: str):
    r = ""
    for i in range(len(x)):
        r += x[i] + " "
    x = r[:len(r)-1]
    return x

def rinput():
    msg = input("Enter a message: ")
    while verif(msg) == False:
        msg = input("Enter a message: ")
    return msg

def rinput2():
    chle = input("Enter The message N2: ")
    while verif(chle) == False or len(msg) != len(chle):
        chle = input("Enter The message N2: ")
    return chle

def crypt(msg,chle):
    mcrypt = ""
    for i in range(len(msg)):
        k = abs(ord(msg[i]) - ord(chle[i]))+1
        oa = chr(97 + k - 1)
        mcrypt +=oa
    mcryptv = esp(mcrypt)
    return mcryptv

def diplay(msg, chle, mcryptv):
    msg2 = esp(msg)
    chle2 = esp(chle)
    print("     " + msg2)
    print("     " + chle2)
    print("     " + mcryptv)

msg = rinput()
chle = rinput2()
esp(msg)
esp(chle)
mcryptv = crypt(msg,chle)
diplay(msg, chle, mcryptv)