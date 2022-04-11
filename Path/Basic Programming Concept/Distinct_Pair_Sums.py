# https://www.codechef.com/LP2TO301/problems/MANYSUMS

t = int(input())
while(t):
    l,r = map(int,input().split())
    if l == r:
        print(1)
    else:
        print((r+r) - (l+l) + 1)
    
    t -= 1