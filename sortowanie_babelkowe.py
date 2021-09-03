if __name__ == "__main__":
    # Sortowanie bąbelkowe:

    lista1 = [4, 2, 5, 10, 1, 7]


    def sortowanie_babelkowe(lista):
        n = len(lista)
        while n > 1:

            zamien = False
            for i in range(0, n-1):
                if lista[i] > lista[i+1]:
                    lista[i], lista[i+1] = lista[i+1], lista[i]
                    zamien = True
            n -= 1

            if zamien == False: break


        return lista

    print(sortowanie_babelkowe(lista1))



