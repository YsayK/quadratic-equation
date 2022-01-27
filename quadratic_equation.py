from math import sqrt as kor


from colorama import Fore
from colorama import init
init()

'''starts and sets all main functions'''
def main():
    x1 = 0.0
    x2 = 0.0
    a = 0
    b = 0
    c = 0

    print()
    print()
    try:
        a = int(input("a number : "))
        b = int(input("b number : "))
        c = int(input("c number : "))
    except ValueError:
        print(Fore.RED + "Error: integers only" + Fore.WHITE)
        main()
    else:
        D = delta_count(a, b, c)
        print()

        print("\nD = " + str(D))

        if D < 0:
            kolvo_x_znazh = 0
            print()
            print(Fore.RED + "no answer" + Fore.WHITE)
            main()
        else:
            '''founds x1 (if D == 0)'''
            if D == 0:
                x1 = (-b + kor(D)) / (2*a)

                print("answer is : x1 = " + Fore.GREEN + f"{x1:.3f}" + Fore.WHITE)
                main()

                '''founds x1 and x2 (if D > 0)'''
            elif D > 0:
                x1 = (-b + kor(D)) / (2*a)

                x1 = (-b - kor(D)) / (2*a)

                print("answer is : x1 = " + Fore.GREEN + f"{x1:.3f}" + Fore.WHITE + " and x2 = " + Fore.GREEN + f"{x2:.3f}" + Fore.WHITE)
                main()

                '''may be Error'''
            else:
                print("Unknown Error")
                main()





'''founds D (discriminant)'''
def delta_count(a, b, c):

    D = b**2 - 4*a*c
    return D







main()
