"""
cryptography.py
Author: Johari
Credit:megsnyder, Noah
Assignment:
Write and submit a program that encrypts and decrypts user data.
See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
l=[]
ll = []
lll=[]
k=()
h=0
g=0 
rr = ("")
e = " " 
while e!= "q": 
    e = input("Enter e to encrypt, d to decrypt, or q to quit: ")
    if e == "q":
        print("Goodbye!")
    elif e == "d": 
        l=[]
        ll = []
        lll=[]
        k=()
        h=0
        g=0 
        rr = ("")
        m = input("Message: ")
        t = input("Key: ")
        for j in m:
            n = (associations.find(j))
            l.append(n)
        for y in t:
                    kk= (associations.find(y))
                    ll.append(kk)
        if len(t)<len(m):
            d = len(m)-len(t)
           
            for g in range(0,d): 
                ll.append(ll[g])
                g+=1
            
        f=len(l)
        x=0
        if len(m) > len(t): 
            while x < len(ll):
                o = l[x] - ll[x]
                
                lll.append(associations[o])
                x+=1
            u=''.join(lll)
            print(u)
        if len(m) < len(t): 
            while x < len(l):
                o = l[x] - ll[x] 
                
                lll.append(associations[o])
                x+=1
            u=''.join(lll)
            print(u)
        
    elif e == "e":
        l=[]
        ll = []
        lll=[]
        k=()
        h=0
        g=0 
        rr = ("")
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
            
        f=len(l)
        x=0
        if len(m) > len(t): 
            while x < len(ll):
                o = ll[x] + l[x] - 2
                
                lll.append(associations[o])
                x+=1
            uu = ''.join(lll)
            print(uu)
        if len(m) < len(t): 
            while x < len(l):
                o = ll[x] + l[x] - 2
                
                lll.append(associations[o])
                uu= rr.join(lll[x])
                x+=1
            print(uu)
    else: 
        print("Did not understand command, try again.") 
