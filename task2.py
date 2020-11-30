#problem 2
def merge(spisok1,spisok2):
    a=[]
    b=0
    for i in range(0, len(spisok1)):
        for g in range (b, len(spisok2)):
            if spisok1[i]<spisok2[g]:
                a.append(spisok1[i])
                break
            else:
                a.append(spisok2[g])
                b+=1
        if b==len(spisok2):
            a.append(spisok1[i])
    for i in range(b,len(spisok2)):
        a.append(spisok2[i])
    return a
