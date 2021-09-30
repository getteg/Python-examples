# алгоритм Евклида NOD на примере поля
# Вариант 1 использую рекурсию
import time
def pole(length, width):
    if length>width:
        if length%width ==0:
            return width
        else:
            length,width = width, length-(width*(length//width))
            return pole(length,width)
    else:
        length,width = width,length
        if length%width == 0:
            return width
        else:
            length,width = width, length-(width*(length//width))
            return pole(length,width)
print(pole(1680,640))

def evklid_nod(a,b):
    if a>b:
        if a%b == 0:
            return b
        else:
            a,b = b, a-(b*(a//b))
            return evklid_nod(a,b)
    else:
        a,b = b,a
        if a%b==0:
            return b
        else:
            a,b = b,a-(b*(a//b))
            return evklid_nod(a,b)

def evklid_nod2(a,b):
    if a<b:
        a,b = b,a
    if a%b ==0:
        return b
    else:
        a,b = b, a%b
        return evklid_nod2(a,b)

start = time.time()
print(evklid_nod2(640,1680))
end = time.time()
print(f'evlkid_nod2 {end-start} сек.' )


# Вариант 2
def get_nod(a,b):
    if a<b:
        a,b = b,a

    while b>0:
        a,b = b, a%b
    return a
start = time.time()
print(get_nod(3,100000000))
end = time.time()
print(f'{end-start} сек.' )
