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

m = " " 
while m!= "q": 
    m = input("Enter e to encrypt, d to decrypt, or q to quit: ")
    for j in m:
        n = associations.find(j)
        l.append(n)
    print(l)
    '''
        for i in n: 
            r = associations[index]    
        
            i+=1
        print([l]
    '''
    if m == "q":
        print("Goodbye!")