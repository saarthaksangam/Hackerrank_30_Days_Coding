t = int(input())
for i in range(0,t):
    s = input()
    t = ''
    for i in range(0,len(s)):
        if(i%2==0):
            t+=s[i]
    t+=' '
    for i in range(1,len(s)):
        if(i%2==1):
            t+=s[i]

    print(t)
        
