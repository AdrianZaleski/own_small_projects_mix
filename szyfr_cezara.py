# Program do szyfrowania wiadomości szyfrem Cezara:

def szyfr_cezara(wiadomosc, klucz):
    # zmienna przechowujaca zaszyfrowana wiadomosc:
    szyfr_wiadomosc = ''
    for x in wiadomosc:
        if x.isalpha():
            liczba = ord(x)  # <- Zmiana znaku na liczbę
            liczba += klucz  # <- Przesuniecie liczby o klucz
            # powrót do reprezentacji znakowej i budujemy wiadomosć zaszyfrowaną:

            if x.isupper():
                if liczba > 90:
                    liczba -= 26
                elif liczba < 65:
                    liczba += 26
            else:
                if liczba > 122:
                    liczba -= 26
                elif liczba < 97:
                    liczba += 26

            szyfr_wiadomosc += chr(liczba)
        else:
            szyfr_wiadomosc += x
    return szyfr_wiadomosc


# wiadomość do szyfrowania:
wiadomosc = input("Podaj swoją wiadomość: ")

# klucz do kodowania:
klucz = int(input("Podaj swoj klucz: "))


print(szyfr_cezara(wiadomosc, klucz))

