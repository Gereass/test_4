N = 0
T = 0

check = False

def checkLen(i):
    return (True if N == len(a) else False)

def countP(z):
    j = 0
    k = 0
    for s,i in enumerate(z):
        if j >= T:
            return (k-1)
        else:
            j = j + i
            k = k + 1
            if s == (len(z) - 1) and j > T:
                return(k-1)
            if s == (len(z) - 1) and j == T:
                return(k)
            
N = int(input())
T = int(input())

while check == False:
    a = [int(i) for i in input().split()]
    check = checkLen(a) 

a = sorted(a)
print(countP(a))
