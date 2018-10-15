"""
cryptography.py
Author: <your name here>
Credit: <list sources used, if any>

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"

l=[]
ll = []
e = " " 
while e!= "q": 
    e = input("Enter e to encrypt, d to decrypt, or q to quit: ")
    m = input("Message: ")
    k = input("Key: ") 
    for j in m:
        n = associations.find(j)
        for y in k:
            kk= associations.find(y)
            ll.append(kk)
            
        l.append(n)
    for f in ll:
        o = [x+f for x in l]
        print(o)
    
    
    '''
        for i in n: 
            r = associations[index]    
        
            i+=1
        print([l]
    '''
    if m == "q":
        print("Goodbye!")