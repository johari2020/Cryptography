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
lll=[]
k=()
h=0
g=0 
e = " " 
while e!= "q": 
    e = input("Enter e to encrypt, d to decrypt, or q to quit: ")
    if e == "q":
        print("Goodbye!")
    else:
        m = input("Message: ")
        kkk = input("Key: ") 
        
                    
        for j in m:
            n = (associations.find(j)+1)
            l.append(n)
        for y in kkk:
                    kk= (associations.find(y)+1)
                    ll.append(kk)
        if len(kkk)<len(m):
            d = len(m)-len(kkk)
           
            for g in range(0,d): 
                ll.append(ll[g])
                g+=1
            print(ll)
        
        
    print(ll)
    print(l)
    f=len(l)
    x=0
    while x < len(ll):
        o = ll[x] + l[x]
        lll.append(associations[o])
        x+=1
    print(lll)
    
    
    if m == "q":
        print("Goodbye!")

"""
cryptography.py
Author: <your name here>
Credit: <list sources used, if any>

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md

associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"

l=[]
ll = []
h=0
e = " " 
while e!= "q": 
    e = input("Enter e to encrypt, d to decrypt, or q to quit: ")
    if e == "q":
        print("Goodbye!")
    else:
        m = input("Message: ")
        k = input("Key: ") 
        for j in m:
            n = (associations.find(j)+1)
            l.append(n)
        for y in k:
            kk= (associations.find(y)+1)
            ll.append(kk)
        print(ll)
        print(l)
"""