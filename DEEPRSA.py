import math
def publickey(phi):
    e=2
    while e<phi:
        if(math.gcd(e,phi)==1):
            break
        else:
            e+=1
    return e
p,q,pt=3,11,9
n=p*q
phi=(p-1)*(q-1)
e=publickey(phi)
d=pow(e,-1,phi)
print(e)
print(d)
ect=pow(pt,e,n)
print(ect)
print(pow(ect,d,n))



