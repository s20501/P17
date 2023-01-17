import math

if __name__ == '__main__':
    # Pobieram dane wejściowe
    fc = float(input("fc(Hz)= "))
    q = float(input("Q= "))

    # Ustalam pojemność kondensatora na 100nF
    c = 100 * (10 ** -9)

    # Obliczam R
    r = 1 / (2 * math.pi * fc * c)

    # Obliczam k dla podanego Q
    k = (3 * q - 1) / q

    # Ustalam R4 na 10kΩ
    r4 = 10000

    # Obliczam R3
    r3 = r4 / (k - 1)

    # Wypisuje wynik
    print(f'R1 = R2 = {int(r)}Ω')
    print('C1 = C2 = 100nF')
    print(f'R3 = {int(r3)}Ω')
    print(f'R4 = 10000Ω')
