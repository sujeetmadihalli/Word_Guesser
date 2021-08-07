
def hangman(a,res,alen,word):
    count=0
    gu_li=[]
    if alen > 20:
        count=10

    elif alen >12:
        count= 7

    elif alen < 13:
        count=5

    print("::::::::::::::: You get " + str(count) + " chances to select a letter and :::::::::::::::")
    print(":::::::: at the end if you did not guess the correct word then ::::::::::")
    print(":::::::::::::::::::::::::::::::::: 'YOU LOSE' :::::::::::::::::::::::::::")
    print("::::: if you guess the correct word before your chances run out :::::::::")
    print(":::::::::::::::::::::::::::::::: 'YOU WIN' ::::::::::::::::::::::::::::::")
    print()
    print()
    print("::::::::::::::::::::::::::: Let's get started :::::::::::::::::::::::::::")
    for guess in range(count):
        print()
        guess=input("Enter the Letter :: ")[0].lower()
        print()
        gu_li.append(guess)
        print("Current guessed letters are :: ", end="")
        for x in gu_li:
            print(x, end=" ")
        print()
        for i in range(alen):
            if guess == a[i]:
                res[i]=guess
                print()
                print("Current word with guessed letters ::  ", end="")
                for x in res:
                    print(x, end=" ")
                print()
                if res == a:
                    return 1
                print()
                abc = input("Do you want to guess the MOVIE name? y/n::").lower()
                print()
                if abc == 'y':
                    print()
                    try_1 = input("Enter the movie name::").lower()
                    print()
                    if try_1 == word:
                        print()
                        print("::::::::::::::::: You guessed it correct ::::::::::::::")
                        print()
                        return 1
                    else :
                        print("No, the movie is not "+ "'" + str(try_1) + "'")
                elif abc == 'n':
                    continue
                print( )
                if res == a:
                    return 1
                print()


    return -1

def numbers_to_strings(argument):
    switcher = {
        1: main(),
    }

    return switcher.get(argument, "nothing")

def exit_program():
    exit()

def main():
    print()
    print()
    word=input("Enter the MOVIE Name(space between will be considered as a character) ::").lower()
    for i in range(100):
        print( )
    a=[]
    for x in word:
        a.append(x)
    alen= len(a)
    res=['_'] * alen
    print()
    print("given word contains "+ str(alen) + " letters")
    print()
    for x in res:
        print( x, end= " ")
    print()
    print()
    result=hangman(a,res,alen,word)
    if result == -1:
        print()
        print("YOU FAILED")
        print("the word was ")
        for x in a:
            print(x, end=" ")
        print()
        print()
    elif result == 1:
        print()
        print(":::::::::::::::HOORAY YOU WON:::::::::::::::")
        print("the word was ")
        for x in a:
            print(x, end=" ")
        print()
    print()
    print("1. If you want to replay the game")
    print("2. If you like to exit the game")
    argument=int(input())
    if argument==2:
        return
    else:
        print(numbers_to_strings(argument))

if __name__ == "__main__":
    main()
    exit()


