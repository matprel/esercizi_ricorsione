
class QuickSort():

    def sort(self, sequenza): #ha come input una lista
        if len(sequenza)<=1:
            return sequenza
        else:
            # 1) scegliere pivot
            pivot = sequenza[0] #scegliamo un elemento a caso

            # 2) dividere la lista in sottoliste (3: più piccoli, uguali, più grandi)
            sequenza_smaller = []
            for i in range(1,len(sequenza)):
                if sequenza[i]< pivot:
                    sequenza_smaller.append(sequenza[i])

            sequenza_pivot = [n for n in sequenza if n == pivot]
            sequenza_larger = [n for n in sequenza if n > pivot]

            # 3) fare il sort delle sottoliste e appendere i risultati
            return (self.sort(sequenza_smaller) +
                    sequenza_pivot +
                    self.sort(sequenza_larger))

if __name__ == '__main__':

    sequenza = [3, 5,0 , 2, 11, 31, 4, 7]
    quicksort = QuickSort()
    print(f"Sequenza non ordinata: {sequenza}")
    print(f"Sequenza ordinata: {quicksort.sort(sequenza)}")
