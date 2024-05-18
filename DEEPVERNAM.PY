def ver(word,key):
    result=[]
    for i in range(len(word)):
        res=((ord(word[i])-65) ^ (ord(key[i])-65))%26
        result.append(chr(res+65))
    return "".join(result)

word = 'HELLO'
key = 'SAKSH'
encrypted_result = ver(word, key)
print(f'Encrypted: {encrypted_result}')
decrypted_result = ver(encrypted_result,key)
print(f'Decrypted: {decrypted_result}')

