# program mający wyświetlać zadaną konstelację giwazdek:

#     * -> 4 spacje + 1 giwazdka
#    ** -> 3 spacje + 2 gwiazdki
#   *** -> 2 spacje + 3 gwiazdki
#  **** -> 1 spacja + 4 gwiazdki
# ***** -> 0 spacji + 5 gwiazdek

n = 5
for i in range(0, n):
    for j in range(0, n-(i+1)):
        print(end=" ")
    for j in range(0, i+1):
        print("*", end = "")  # <- Uwaga tutaj było bez spacji i zadziałało!
    print("\r")





# Program do utworzenia symetrycznego trójkąta z gwiazdek:
#     *
#    * *
#   * * *
#  * * * *
# * * * * *

n = 6
for i in range(0, n):
    for j in range(0, n-(i+1)):
        print(end=" ")
    for j in range(0, i+1):
        print(" ", end = "*")
    print("\r")
