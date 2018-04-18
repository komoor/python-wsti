# a = input("Podaj swoje imie: ")
# b = int(input("Podaj swoj wiek: "))

# if b == 18:
#     print("jestes pelnoletni" + a)
# elif b == 25:
#     print("Zaraz zakonczysz studia " + a)
# else: 
#     print("sorry")


# a = 1 
# while a <= 10:
#     print(a)
#     a += 1

# numerki = [1,2,3,4,5,6] 

# for numer in numerki: 
#     print(numer) 

# for x in range(1,20):
#     if x == 15: 
#         break
#     print(x)

# words = ['WSTI',' ', 'studia'] 

# for slowo in words:
#     for literka in slowo:
#         print(literka)

import math

promien = float(input("podaj promien: ")) 

wynik = math.pi * promien * promien 

print("Pole to: " + str(wynik))