x=2

if x==2:
    print ('le test est vrai')
else :
    print ("le test est faux")

a = "bonjour"
print(a)

def Sum_moy(LISTE):
    Sum = 0
    for val in LISTE:
        Sum += val
    moy = round(Sum/len(LISTE), 1)
    return Sum, moy 

Sum_moy([-1, 3, 4, -1])   
