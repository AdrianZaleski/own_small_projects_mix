if __name__ == "__main__":

    # Progam wypisuje liczby od 1 do 20,
    #     liczby podzielne przez 3 zamienić słowem Fizz
    #     liczby podzielne przez 5 zmienić na Buzz
    #     liczby podzielne przez 3 i przez 5 - FizzBuzz

    # for i in range(1, 21):
    #     if i % 3 == 0 and i % 5 == 0:
    #         print(f"FizzBuzz")
    #     elif i % 3 == 0:
    #         print("Fizz")
    #     elif i%5 == 0:
    #         print("Buzz")
    #     else:
    #         print(i)

    # ####------------------ZADANIE 2------------------------------------###################

    # #### Należy znaleźć najmniejszą oraz największa liczbę na liście

    # najwieksza = None
    # najmniejsza = None
    #
    # lista = [1, 3, 7, 11, 2, -6, 0]
    #
    # for i in lista:
    #     if najmniejsza == None or najmniejsza > i:
    #         najmniejsza = i
    #     if najwieksza == None or i > najwieksza:
    #         najwieksza = i
    #
    # print(f"Największa wartość z listy to {najwieksza}\n"
    #       f"Najmniejsza wartość to: {najmniejsza}")

    # ####------------------ZADANIE 3------------------------------------###################

    # Mamy podany ciąg S. Np „Ala ma kota”. W ramach zadania możemy zostać poproszeni o jedno, lub więcej z poniższych:
        # 1. zliczyć wyrazy. W naszym przypadku będzie ich 3
        # 2. zliczyć litery. Będzie ich 9
        #3. zbadać częstotliwość występowania liter. a – 3, l – 1, m 1, k – 1, t – 1
    #
    # zdanie =  input("Podaj zdanie do policzenia: ")
    # ilosc_liter = 0
    #
    # # Zliczenie liczby liter i innych znaków oprócz spacji:
    # for i in zdanie:
    #     if i == " " :
    #         continue
    #     else:
    #         ilosc_liter += 1
    #
    # print(f"Ilość liter w podanym zdaniu wynosi: {ilosc_liter}")
    #
    # # zliczenie słów w zdaniu:
    # wyrazy = zdanie.split()
    # pomoc = {}
    # for i in wyrazy:
    #     pomoc[i] = wyrazy.count(i)
    # print(f"ilość słów w zdaniu wynosi: {len(pomoc)}")
    #
    # # zliczanie wystepowania liter w zdaniu:
    # slownik = {}
    # print(zdanie)
    # print(slownik)
    # for i in zdanie:
    #     slownik[i] = zdanie.count(i)
    # print(slownik)


    # ####------------------ZADANIE 4------------------------------------###################
    #Utworz program pytajacy się człoweiak o wiek.
    # Wypisz wiadomość zaadresowaną do nich i mówiącą w którym roku skończą 100 lat.

    # wiek = int(input("Podaj swój aktualny wiek: "))
    # Do_setki = 100 - wiek
    #
    # if Do_setki < 0:
    #     print("Przecież już miałeś sto lat!")
    # else:
    #     data = 2021 + Do_setki
    #     print(f"Wiek 100 lat osiągniesz w {data} roku")

    # ####------------------ZADANIE 5 -----------------------------------###################
    #Wypisz wartości z listy mniejsze niż wartość wpisana przez użytkownika
    # Zapisz wyniki w nowej liście

    # lista = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    #
    # mniejniz = int(input("Podaj wartość dla której spiszemy mniejsze: "))
    # lista_mniejsza = []
    #
    # for i in lista:
    #     if i < mniejniz:
    #         lista_mniejsza.append(i)
    # print(lista_mniejsza)
    #
    #

    # #####--------------ZADANIE 6 ---------------------------------#####
    # # Odwróć wyrazy w tekście
    #
    # tekst = 'Jakiś tekst do podzielenia, CO z tego wyjdzie nie wiem'
    # tekst_odw_pom = []
    # wyrazy = tekst.split(' ')  # <- Utworzenie listy z podzielonych wyrazów na osobne elementy
    # 
    # for slowo in tekst.split(' '):
    #     tekst_odw_pom.append(slowo[::-1])
    #
    # tekst_odw = ' '.join(tekst_odw_pom)
    # print(tekst_odw)
    #
    # # Wersja ONE_LINER:
    # print(' '.join(slowo[::-1] for slowo in tekst.split(' ')))