from time import sleep

def Tour_Hanoi_console(n,solution):
    poteaux = [[n-i for i in range(n)],[],[]]
    print(f'Tour de Hanoï avec {n} disques\n')
    affichage_console(n,poteaux)
    while len(solution) > 0:
        mouvement = solution.pop(0)
        poteaux[mouvement[2]-1].append(mouvement[0])
        poteaux[mouvement[1]-1].pop()
        affichage_console(n,poteaux)

def affichage_console(n,poteaux,t=0.1):
    affichage = '\n'
    for poteau in poteaux:
        for i in range(n-len(poteau)):
            poteau.append(0)
    for i in range(1,n+1):
        for poteau in poteaux:
            k = poteau[n-i]
            affichage += f' '*(n-k) + '-'*k + '|' + '-'*k +  ' '*(n-k)
            #affichage += f' '*(n-k) + '-'*k + str(k) + '-'*k +  ' '*(n-k)
        affichage += '\n'
    for poteau in poteaux:
        for i in range(n):
            if poteau[n-i-1] == 0:
                poteau.pop()
    sleep(t)
    print(affichage)
   
    