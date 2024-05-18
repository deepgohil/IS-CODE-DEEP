def ces(k,msg,flag):
    res=""
    for i in range(len(msg)):
        c_char=msg[i]
        if(flag):
            res+=chr((ord(c_char)-97+k)%26+97)
        else:
            res+=chr(ord(c_char)-k) 
    return res



pt = "gharpe"
# pt=pt.lower()
encrypted = ces(3,pt,True)
print(encrypted)
decrypted = ces(3,encrypted,False)
print(decrypted)
