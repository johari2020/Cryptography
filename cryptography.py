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
    elif e == "d": 
        print(3)
    elif e == "e":
        m = input("Message: ")
        t = input("Key: ") 
        
                    
        for j in m:
            n = (associations.find(j)+1)
            l.append(n)
        for y in t:
                    kk= (associations.find(y)+1)
                    ll.append(kk)
        if len(t)<len(m):
            d = len(m)-len(t)
           
            for g in range(0,d): 
                ll.append(ll[g])
                g+=1
            print(ll)

        print(l)
        f=len(l)
        x=0
        if len(m) > len(t): 
            while x < len(ll):
                o = ll[x] + l[x] - 2
                if o > len(associations):
                    p = o - len(associations) 
                else: 
                    p=o
                lll.append(associations[p])
                x+=1
            print(lll)
        if len(m) < len(t): 
            while x < len(l):
                o = ll[x] + l[x] - 2
                if o > len(associations):
                    p = o - len(associations) 
                else: 
                    p=o
                lll.append(associations[p])
                x+=1
            print(lll)
    else: 
        print("try again") 

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