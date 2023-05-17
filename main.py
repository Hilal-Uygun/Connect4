import numpy as np
import random

stamps = ['p','y']
table = np.chararray((9,9))
table[:] = 'o'
table_non_b = np.char.decode(table)
np.savetxt('Tahta.txt', table_non_b, fmt='%s')

def giris():
    print('Welcome to the Connect 4 game\n')
    global name1, name2, stamp1, stamp2
    name1 = input('Please write your nick ')
    name2 = input('Please write your nick ')

    stamp = random.choice(stamps)
    stamp1 = stamp

    if(stamp1 == 'p'):
        stamp2 = 'y'
    else:
        stamp1 = 'y'
        stamp2 = 'p'

    print(f'{name1}, your stamp is {stamp1}')
    print(f'{name2}, your stamp is {stamp2}')

#Bu fonksiyonda hamleler siliniyor.
def reset_hamle():
    with open('Hamle.txt', 'w') as file:
        pass
#----------------------------
def reset_tahta():
    global table, table_non_b
    table[:] = 'o'
    table_non_b = np.char.decode(table)
    np.savetxt('Tahta.txt', table_non_b, fmt='%s')

#Slot boş mu ve hamle kaydetme fonksiyonu
def hamle(i,j,name):
    f = open('Hamle.txt', 'a')
    f.write(f'{name} {i+1}{j+1}\n')

#-----------------------------------------------------
def arrangement(namee, stampp):
    hamlee = int(input(f'{namee} write your move ')) - 1
    for row in reversed(range(9)):
        if (table_non_b[(row, hamlee)] == 'o'):
            table_non_b[(row, hamlee)] = stampp
            hamle(row, hamlee, namee)
            break
        if (row == 0 and table_non_b[(row, hamlee)] != 'o'):
            print('You cannot choose this slot!')
            hamlee = int(input(f'{namee} write your move ')) - 1
            for row in reversed(range(9)):
                if (table_non_b[(row, hamlee)] == 'o'):
                    table_non_b[(row, hamlee)] = stampp
                    hamle(row, hamlee, namee)
                    break
            np.savetxt('Tahta.txt', table_non_b, fmt='%s')

    np.savetxt('Tahta.txt', table_non_b, fmt='%s')

    print('\n')
    f = open("Tahta.txt", "r")
    print(f.read())

#Kazananı bul
def move(name):
    #dikey
    for row in range(6):
        for col in range(9):
            if(table_non_b[(row,col)] != 'o' and table_non_b[(row,col)] == table_non_b[(row+1,col)] == table_non_b[(row+2,col)] == table_non_b[(row+3,col)]):
                return True

    #yatay
    for row in range(9):
        for col in range(6):
            if(table_non_b[(row,col)] != 'o' and table_non_b[(row,col)] == table_non_b[(row,col+1)] == table_non_b[(row,col+2)] == table_non_b[(row,col+3)]):
                return True
    #/
    for row in range(6):
        for col in range(3,9):
            if(table_non_b[(row,col)] != 'o' and table_non_b[(row,col)] == table_non_b[(row+1,col-1)] == table_non_b[(row+2,col-2)] == table_non_b[(row+3,col-3)]):
                return True
    #\
    for row in range(6):
        for col in range(6):
            if(table_non_b[(row,col)] != 'o' and table_non_b[(row,col)] == table_non_b[(row+1,col+1)] == table_non_b[(row+2,col+2)] == table_non_b[(row+3,col+3)]):
                return True
#-----------------------------------------------------
giris()
while True:
    exit = input("Write for playing game 'g', for exit 'e'").lower()
    if (exit == 'e'):
        choice = input('Write c for CONTINUE or write n for NEW GAME ').lower()
        if (choice == 'c'):
            print('\n')
            f = open("Tahta.txt", "r")
            print(f.read())
            arrangement(name1,stamp1)
            if (move(name1)):
                print(f'{name1} is the winner!')
                reset_hamle()
                reset_tahta()
                break

            exit = input("Write for playing game 'g', for exit 'e'").lower()
            if (exit == 'e'):
                choice = input('Write c for CONTINUE or write n for NEW GAME ').lower()
                if (choice == 'c'):
                    print('\n')
                    f = open("Tahta.txt", "r")
                    print(f.read())
                    arrangement(name2, stamp2)
                    if (move(name2)):
                        print(f'{name2} is the winner!')
                        reset_hamle()
                        reset_tahta()
                        break
                else:
                    reset_hamle()
                    reset_tahta()
                    giris()
            else:
                arrangement(name2, stamp2)
                if (move(name2)):
                    print(f'{name2} is the winner!')
                    reset_hamle()
                    reset_tahta()
                    break
        else:
            reset_hamle()
            reset_tahta()
            giris()

    elif(exit == 'g'):
        print('\n')
        f = open("Tahta.txt", "r")
        print(f.read())

        arrangement(name1,stamp1)
        if (move(name1)):
            print(f'{name1} is the winner!')
            reset_hamle()
            reset_tahta()
            break
        exit = input("Write for playing game 'g', for exit 'e'").lower()
        if (exit == 'e'):
            choice = input('Write c for CONTINUE or write n for NEW GAME ').lower()
            if (choice == 'c'):
                print('\n')
                f = open("Tahta.txt", "r")
                print(f.read())
                arrangement(name2, stamp2)
                if (move(name2)):
                    print(f'{name2} is the winner!')
                    reset_hamle()
                    reset_tahta()
                    break
            else:
                reset_hamle()
                reset_tahta()
                giris()
        else:
            arrangement(name2, stamp2)
            if (move(name2)):
                print(f'{name2} is the winner!')
                reset_hamle()
                reset_tahta()
                break
    else:
        print('Invalid choice. Try again')
        exit = input("Write for playing game 'g', for exit 'e'").lower()