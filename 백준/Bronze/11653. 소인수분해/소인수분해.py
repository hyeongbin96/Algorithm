N = int(input())

i = 2
while True :
    if N == 1 :
        break 
    elif N % i == 0 :
        N = N / i
        print(i)
    else :
        i += 1