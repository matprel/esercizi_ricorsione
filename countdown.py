from time import sleep

#l'input è un intero, vogliamo che questa funzione conti fino a 0
def countdown(n): #caso iterativo
    counter = n
    while counter >=0 : #decrementa la variabile fino ache non arriva a 0
        print(counter)
        # sleep(1) stampa più lenta
        counter -= 1


def countdown_recursive(n):
    if n <= 0: #condizione terminale
        print("Stop")
    else:
        print(n)
        # sleep(1)
        countdown_recursive(n-1)

if __name__ == '__main__':
    countdown(10)
    countdown_recursive(10)


