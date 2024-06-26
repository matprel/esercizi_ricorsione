def palindrome(word): #parola che è uguale se è lettada dx verso sx e da sx verso dx
    if len(word)<=1: #se ha una lettera, è sicuramente un palindromo
        return True
    else: #altrimenti verifico se la prima e l'ultima lettera sono uguali e richiamo la funzione su quello che c'è in mezzo
        return word[0]==word[-1] and palindrome(word[1:-1]) #se le due lettere non sono uguali return False

def palindrome_banale(word):
    return word==word[::-1]

if __name__ == '__main__':
    print(palindrome("casa"))
    print(palindrome("civic"))
    print(palindrome_banale("civic"))