# https://www.codechef.com/LP2TO301/problems/MINPIZZAS

import math
t = int(input())
while(t):
    n,k = map(int,input().split())
    print(int(n//math.gcd(n,k)))
    t -= 1

# Watch video for better understanding.