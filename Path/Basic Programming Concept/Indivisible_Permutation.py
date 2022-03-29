# https://www.codechef.com/LP2TO301/problems/INDIPERM

# My Solution same as the Standard: 
t = int(input())
while(t):
    n = int(input())
    if n>1:
        for i in range(2,n+1):
            print(i,end=" ")
        print(1)
    else:
        print(1)
    
    t -= 1