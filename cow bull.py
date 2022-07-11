import random
def nonrepeat():
    x=str(random.randrange(1000,9999,1))
    c=0
    for i in x:
        if x.count(i)>1:
            c=c+1
    if c>=1:
        return nonrepeat()
    else:
        return x
def inputrepet(y):
    L = list(y)
    count = 0
    for i in L:
        if L.count(i) > 1:
            count = count + 1
    if count>=1:
        print('digits must be non-repetive')
        k=input('input another number:')
        return inputrepet(k)
    else:
        return y
x=nonrepeat()
y=input('GUESS THE NUMBER:')
y=inputrepet(y)
c = b = 0
while (b != 4):
    for i in range(4):
        for j in range(4):
            if x[i] == y[j] and i == j:
                b = b + 1
            elif x[i] == y[j]:
                c = c + 1
    if b == 4:
        print('.................YOU WON ..............')
        break
    else:
        print('YOU GOT ' + str(b) + ' BULL AND ' + str(c) + ' COW')
        a = input('TRY ANOTHER NUMBER BUDDY:')
        a=inputrepet(a)
        y = a
    c = b = 0