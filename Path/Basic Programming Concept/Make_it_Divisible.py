# https://www.codechef.com/LP2TO301/problems/MAKEDIV3

t = int(input())
while(t):
    n = int(input())
    print(3,end="")
    for i in range(n-2):
        print(0,end="")
    if (n>=2):
        print(3,end="")
    print()
    
    t -= 1