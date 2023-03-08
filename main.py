import sys
from faker import Faker

faker = Faker('pl_PL')

no_of_tries = int(input("Podaj ile prob chcesz mieć: "))
word = faker.word() #tworzy losowe slowo
used_letter = []
user_word = []

def find_indexes(word, letter):
    """znajduje indexy liter w slowie"""
    indexes = []
    for index, letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indexes.append(index)
    return indexes


def show_state_of_game():
    """wyswietla statystyki gry"""
    print()
    print(user_word)
    print("Pozostało prób:", no_of_tries)
    
    if no_of_tries == 0:
        print("Koniec gry.")
        sys.exit(0)

for _ in word:
    user_word.append('_')

while True:
    letter = input("Podaj literę: ")
    if letter.isalpha() == True:  #sprawdza, czy wprowadzona jest litera
        if letter in used_letter:  #sprawdza, czy litery sie nie powtarzaja
            print("Podałeś już tą literę wczesniej.")
            no_of_tries -=1
        else:
            used_letter.append(letter)

        found_indexes = find_indexes(word, letter)

        if len(found_indexes) == 0:
            print("Nie ma takiej litery.")
            no_of_tries -= 1

        else: 
            for index in found_indexes:
                user_word[index] = letter

            if "".join(user_word) == word:
                print(f"Brawo, udało Ci się odgadnąć słowo: {word}")
                sys.exit(0)

        show_state_of_game()

    else:
        print("Musisz podać litere.")
        






