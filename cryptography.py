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
            for g in ll:
                gg = ll.append(g)
                g+=1
            print(gg)
        
        
    print(ll)
    print(l)
    for f in l:
        for w in ll:
            o = w+f
            lll.append(o)
            w+=1
        f+=1
    print(lll)
    
    '''
        for i in n: 
            r = associations[index]    
        
            i+=1
        print([l]
    '''
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