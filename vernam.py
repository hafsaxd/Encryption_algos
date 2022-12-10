import random  
import string 

#Generate random key everytime 
def generateRandomKey(length):  
    sample_string = 'pqrstuvwxy' 
    # define the condition for random string  
    result = ''.join((random.choice(sample_string)) for x in range(length))  
    return result 
  
def makeVernamCypher( text, key ):
    cipher = "" # the Cipher text
    p = 0 # pointer for the key
    for char in text:
        #performing XOR operation
        XOR_vernam = ord(char) ^ ord(key[p])
        cipher += chr(XOR_vernam)
        p += 1

        #once key length has reached then plaintext, reappend the key 
        if p==len(key):
            p = 0
    return cipher

                      
KEY = generateRandomKey(16)
while True:
    print("\n\n---Vernam Cypher---")
    PlainText = input("Enter text to encrypt: \n")

    print("encrypting " + PlainText + " ...")
    # Encrypt
    Cipher = makeVernamCypher(PlainText, KEY)
    print("encrypted text  : " + Cipher) 
    # Decrypt
    decrypt = makeVernamCypher(Cipher, KEY)

    print("\ndecrypting  back ... ")
    print("Decrypted text : "+decrypt)
