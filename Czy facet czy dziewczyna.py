
def main():
    imie = input("Podaj swoje imie: ")


    imie = imie.casefold()
    imie = list(imie)

    print(imie)

    if imie[-1] == 'a':
        print("\nJesteś dziewczyną!")
    else:
        print("\nJesteś facetem!")

    repeat = print(input("Czy chcesz ponowic program? (y/n): "))
    if repeat == 'n':
        exit()
    
    else:
        main()

    main()
    #exit()
main()


