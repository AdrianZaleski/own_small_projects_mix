"""
ZADANIE 2. PODANA JEST LISTA ZAWIERAJĄCA ELEMENTY O WARTOŚCIACH 1-n.
NAPISZ FUNKCJĘ KTÓRA SPRAWDZI JAKICH ELEMENTÓW BRAKUJE

1-n = [1,2,3,4,5,...,10]
np. n=10
wejście: [2,3,7,4,9], 10
wyjście: [1,5,6,8,10]
"""

if __name__ == "__main__":

    def list_with_lack_of_values():
        intake = [[2, 3, 7, 4, 9], 10]
        n = intake[1]
        basic_list = [i for i in range(1, n + 1)]

        for entered in intake[0]:
            for basic_value in basic_list:
                if entered == basic_value:
                    basic_list.remove(entered)
        return basic_list


    print(list_with_lack_of_values())
