demoni=[]
stamine=[]
def maxim(a, b):
    if a>b:
        return a
    return b

def minim(a,b):
    if a>b: return b
    return a


def binary_search(x, st, dr):
    mid=-1
    while st<dr:
        mid = (st + dr) // 2 +1
        if x<demoni[mid][1]:
            dr=mid-1
        else: st=mid
    if demoni[st][1]<=x:
        return st
    return -1


# 0 pt indice
# 1 pt stamina necesara
# 2 pt cate ture pana primesc stamina
# 3 pt stamina primita
# 4 pt nr puncte
with open("in.txt") as f:
    stam_st, stam_max, turns, n=map(int, f.readline().split())
    for i in range(n):
        demoni.append([i])
        line=[int(x) for x in f.readline().split()]
        demoni[i].extend(line[:4])
        if line[3]!=0:
            prec=line[4]
        for x in line[4:]:
            x+=prec
            demoni[i].extend([x])
            prec=x
        # demoni[i].extend(line)
# for x in demoni:
#     print(x)
f=open("output.txt", 'w')
demoni.sort(key=lambda x:x[1])
# for x in demoni:
#     print(x)
import time
start=time.time()
suma=0
for t_curent in range(turns):
    for x in stamine:
        if t_curent==x[0]:
            stam_st=minim(x[1]+stam_st, stam_max)
    start_cautare=binary_search(stam_st, 0, n-1)
    # print(start_cautare)
    max=-1
    index_max=0
    if start_cautare!=-1:
        for i in range(start_cautare+1):
            if demoni[i][0]!=-1:
                if demoni[i][2]>turns-t_curent:
                    par2=-2
                else: par2=1-(demoni[i][2]/demoni[i][3])
                suma_demon=demoni[i][minim(turns-t_curent+4,len(demoni[i])-1)]
                if suma!=0:
                    par1=1-(1/suma)
                else: par1=-2
                # valoare=maxim(par1, par2)
                valoare=suma_demon
                if valoare>max:
                    max=valoare
                    index_max=i
                    suma_max=suma_demon
    if max!=-1:
        suma+=suma_max
        f.write(f"{demoni[index_max][0]}\n")
        stam_st-=demoni[index_max][1]
        stamine.append([demoni[index_max][2]+t_curent, demoni[index_max][3]])
        demoni[index_max][0]=-1
    finish=time.time()
    if finish-start>120:
        break
for el in demoni:
    if el[0]!=-1:
        f.write(f"{el[0]}\n")
print(suma)