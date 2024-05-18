def mEncode(msg,key):
    res=[]
    for i in range(len(msg)):
        ans=((ord(msg[i])-65)+(ord(key[i])-65))%26
        res.append(chr(ans+65))
    return "".join(res)

def mDncode(msg,key):
    res=[]
    for i in range(len(msg)):
        ans=(((ord(msg[i])-65)-(ord(key[i])-65))+26)%26
        res.append(chr(ans+65))
    return "".join(res)


if __name__ == "__main__":
    string = input("Enter your message: ").upper().replace(" ", "")
    keyword = input("Enterkey:").upper().replace(" ", "")
    cipher_text = mEncode(string, keyword)
    print("Ciphertext :", cipher_text)
    print("Original/DecryptedText:", mDncode(cipher_text, keyword))