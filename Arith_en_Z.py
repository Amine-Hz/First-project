from time import *
import re

restes = []

def div(a,b):
    try:
        return b%a == 0
    except ZeroDivisionError:
        if english:
            print("Division by zero is impossible!!")
        else:
            print("La division par 0 est impossible!!")

def D(*args):
    Dvs = []
    if isinstance(args[0],list):
        args = args[0]
    if len(args) == 1:
        if args[0]!=0:
            a = args[0] if args[0]>0 else -args[0]
            for n in range(-a,a+1):
                if n != 0:
                    if div(n,a):
                        Dvs.append(n)
            return Dvs
        else:
            raise(Exception("D(0) = ℤ"))
    else:
        cdvs = []
        for a in args:
            cdvs.append(D(a))
        for i,d in enumerate(cdvs):
            if d != cdvs[-1]:
                cdvs[i+1] = set(d) & set(cdvs[i+1])
        return sorted(list(cdvs[-1]))
    


def bezout(a, b):
    a_signe = int(a>0) - int(a<0)
    b_signe = int(b>0) - int(b<0)
    a, b = abs(a), abs(b)
    r, r_prev = a, b
    u, u_prev = 1, 0
    v, v_prev = 0, 1

    while r_prev != 0:
        q = r // r_prev
        r, r_prev = r_prev, r - q * r_prev
        u, u_prev = u_prev, u - q * u_prev
        v, v_prev = v_prev, v - q * v_prev
    return u * a_signe, v * b_signe

def solve(equation, testing = False):
    #Fetching required parametres
    pattern = r'[+-]?\d*\.?\d*[a-zA-Z]?'
    matches = re.findall(pattern, equation)
    equ = [str for str in matches if str]
    a, b, c = equ
    a, b, c = int(a[:-1]), int(b[:-1]), int(c)
    #Start of the algorithm
    d = PGCD(a,b)
    if not div(d,c):
        return 'S= ∅' if not testing else 0
    a0, b0, c0 = int(a/d), int(b/d), int(c/d)
    u, v = bezout(a0,b0)
    x0, y0 = u*c0, v*c0
    a0 = -a0
    return 'S = { ( x = ('+str(b0)+')k+('+str(x0)+') ; y = ('+str(a0)+')k+('+str(y0)+') ) / k∈ℤ }' if not testing else (b0,x0,-a0,y0)


def PGCD(a, b, euclide = False):
    if euclide:
        a,b=abs(a),abs(b)
        r = max(a,b)%min(a,b)
        if r != 0:
            restes.append(r)
            return PGCD(r,min(a,b))
        return restes[-1] if len(restes)>0 else min(a,b)
    else:
        return max(set(D(a))&set(D(b)))

def PPCM(a,b):
    return int(a*b/PGCD(a,b))

def det_PGCD():
    if english:
        print("Let's find out what is the PGCD of a and b:\n")
    else:
        print("Determinons le PGCD de a et b:\n")
    a = int(input("a = "))
    b = int(input("b = "))
    pgcd = PGCD(a,b, euclide=True)
    print(f"\nPGCD({a},{b}) =", pgcd)
    if pgcd == 1:
        if english:
            print("PS: These two numbers are prime with each other!")
        else:
            print("Remarque: Ces deux nombres sont premiers entre eux!")
        
def det_PPCM():
    if english:
        print("Let's find out the PPCM of a and b:\n")
    else:
        print("Determinons le PPCM de a et b:\n")
    a = int(input("a = "))
    b = int(input("b = "))
    print(f"\nPPCM({a},{b}) =", PPCM(a,b))
        
def det_D():
    if english:
        choice = input('''If you want to calculate the divisors of a enter a\nIf you want to calculate the common divisors of many numbers enter any other letter.''')
        print("Let's find out the divisors of a or the divisors of many numbers!!\n")
    else:
        choice = input('''Si vous voulez determiner les diviseurs de a cliquez a puis enter\nSi vous voulez determiner les diviseurs communs de plusieurs nombres cliquez n'importe quelle autre lettre puis entrer ''')
        print("Determinons les diviseurs de a ou les diviseurs communs de plusieurs nombres!!\n") 
    if choice == 'a':
        a = int(input(("\na = ")))
        print(f"D({a}) =",D(a))
    else:
        if english:
            print("Press enter when you finish entering all numbers")
        else:
            print("Cliquez entrer si vous avez terminez d'entrer les nombres")
        inputs = []
        for ltr in "abcdefghijklmnopqrstuvwxyz":
            inp = input('\n'+ltr+" = ")
            if inp == "":
                print('\r')
                break
            inputs.append(inp)
        inputs = [int(x) for x in inputs]
        print(f"D({str(inputs)[1:-1]}) = {D(inputs)}")

def det_div():
    if english:
        print("Does a devide b??")
    else:
        print("Est-ce que a divise b??")
    a = int(input("a = "))
    b = int(input("b = "))
    if div(a,b):
        if english:
            print(f"Yes, {a} does devide {b}!")
        else:
            print(f"Oui, {a} divise {b}!")
    else:
        if english:
            print(f"No, {a} does not devide {b}")
        else:
            print(f"Non, {a} ne divise pas {b}")
            
def det_solve():
    if english:
        equation = input('Write the equation in the form of "ax+by=c" such that a, b and c ∈ ℤ* :\n')
    else:
        equation = input('Ecrivez l\'equation sous forme de "ax+by=c" tel que a, b et c ∈ ℤ* :\n')
    try:
        solution = solve(equation)
        print(solution)
    except Exception as e:
        if str(e) == 'D(0) = ℤ':
            if english:
                print("a,b and c ∈ ℤ*, this means that none of them can be 0")
            else:
                print("a,b et c ∈ ℤ*, c.à.d qu'aucun d'entre eux ne peut être 0")
        elif str(e) == 'too many values to unpack (expected 3)':
            if english:
                print("Please write the equation in the form ax+bx=c only.\nThis means that these are valid:\n 12x+24y=48 \n -12x+24y=48 \n 12x-24y=48 \n 12x+24y=-48")
            else:
                print("Svp écrivez l'equation seulement sous la forme ax+bx=c.\nC.à.d que ces équations sont valides:\n 12x+24y=48 \n -12x+24y=48 \n 12x-24y=48 \n 12x+24y=-48")
        elif str(e) in ["invalid literal for int() with base 10: '+'", "invalid literal for int() with base 10: '-'", "invalid literal for int() with base 10: ''"]:
            if english:
                print("If you attempted to write x+y=c, please note that it should be written as the following: 1x+1y=c")
            else:
                print("Si vous avez tenté d'écrire x+y=c, veuillez noter qu'il doit être écrit comme suit : 1x+1y=c")
        else:
            raise e

def main():
    again = True
    while again:
        language = input("English?? Français??\n Type your language of choice/Ecrivez votre langue de choix:\n").lower()
        global english
        if language == "english":
            english = True
            again = False
        elif language == "francais" or language == "français":
            english = False
            again = False
        else:
            print('Please only input "english" or "français"/Merci de saisir uniquement "english" ou "français"')
            again = True
    if english:
        print("Welcome to Arithmetic In Z!!")
    else:
        print("Bienvenue dans Arithmétique Dans Z!!")
    sleep(1)
    if english:
        print("This program contains some useful functions in this math chapter\n")
    else:
        print("Ce programme contient des fonctions utiles dans ce chapitre\n")
    sleep(1.5)
    loop = 1
    while loop:
        if english:
            print("Enter: pgcd to calculate the PGCD using Euclide's algorithm")
            print(' '*7+"'ppcm' to calculate the PPCM of two numbers")
            print(' '*7+"'div' to see if a number devides another")
            print(' '*7+"'d' to calculate the set of divisors D() of one or more numbers")
            print(' '*7+"'equa' to solve a diophantine equation")
            choix = input('\nChoice = ').lower()
            print('\n')
        else:
            print("Entrez: pgcd pour determiner le PGCD par l'Algorithme d'Euclide")
            print(' '*8+"'ppcm' pour determiner le PPCM de deux nombres")
            print(' '*8+"'div' pour voir si un nombre divise l'autre")
            print(' '*8+"'d' pour determiner l'ensemble des diviseurs D() d'un ou plusieurs nombres")
            print(' '*8+"'equa' pour résoudre une équation diophantienne")
            choix = input('\nChoix = ').lower()
            print('\n')
        if choix == 'pgcd':
            det_PGCD()
        elif choix == 'ppcm':
            det_PPCM()
        elif choix == 'div':
            det_div()
        elif choix == 'd':
            det_D()
        elif choix == 'equa' or choix == 'équa':
            det_solve()
        else:
            if english:
                print('Please input either "pgcd" or "ppcm" or "div" or "d"')
            else:
                print('Veuillez saisir soit "pgcd" soit "ppcm" soit "div" soit "d"')
        sleep(2)
        if english:
            loop = int(input("\nIf you want to choose another function, enter 1, if not then enter 0: "))
        else:
            loop = int(input("\nSi vous voulez choisir une autre fonction, entrez 1, sinon entrez 0: "))
    if english:
        print("See ya later!!")
    else:
        print("Au revoir!!")
    sleep(1)

if __name__ == '__main__':
    main()



