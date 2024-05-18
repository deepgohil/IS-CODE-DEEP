import math
import hashlib
def finde(phi):
    e=2
    while e<phi:
        if(math.gcd(e,phi)==1):
            break
        else:
            e+=1
    return e

p=3
q=11
pt=9
n=p*q
phi=(p-1)*(q-1)

e=finde(phi)
d=pow(e,-1,phi)

# sender side
message=input("enter message")
inputdata=bytes(message,'utf-8')

hash_val=hashlib.sha256(inputdata).hexdigest()
hash_val=int(hash_val,16)%n

digsig=pow(hash_val,d,n)

# rceiver side
hash_val_check=pow(digsig,e,n)

print(f"{hash_val}  =======   {hash_val_check}")



