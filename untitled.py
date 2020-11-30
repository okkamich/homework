#problem1
def task1(spisok,chislo):
    a=[]
    for i in range (0, len(spisok)):
        if spisok[i]==chislo:
            a.append(i)
    return a
