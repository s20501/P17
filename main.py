import math

import matplotlib.pyplot as plt


def frf(f, c, r):
    # Przygotowanie danych pod wykres
    c1, c2, r1, r2 = c, c, r, r
    # Częstość graniczna,
    w = 2 * math.pi * f
    num = 1 / (c1 * c2 * r1 * r2)
    den = 1 / (c1 * c2 * r1 * r2) + (r1 + r2) / (c1 * r1 * r2) * 1j * w - w ** 2
    return num / den


def dB(x):
    # Zwraca wartość w decybelach
    return 20 * math.log10(abs(x))


# Główna pętla programu
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

    plt.figure()

    target = (fc, dB(frf(fc, c, r)))

    freqs = range(1000000)  # zakres 0 Hz do 1 MHz
    response = [dB(frf(f, c, r)) for f in freqs]

    ax = plt.subplot(2, 1, 1)
    plt.semilogx(freqs, response)
    plt.semilogx(target[0], target[1], ms=10)
    plt.title('LPF')
    plt.xlabel('[Hz]')
    plt.ylabel('[dB]')

    lims = list(ax.get_ylim())
    lims[1] = 20
    plt.ylim(lims)

    plt.show()
