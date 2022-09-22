def print_field(a):
    print(' '+a[0]+' | '+a[1]+' | '+a[2]+'  ')
    print('---|---|---')
    print(' '+a[3]+' | '+a[4]+' | '+a[5]+'  ')
    print('---|---|---')
    print(' '+a[6]+' | '+a[7]+' | '+a[8]+'  ')


def inp():
   return int(input('Ваш ход (от 1 до 9): '))-1
    
    
def check(a,n1,n2,n3):
    if (a[n1]==a[n2]==a[n3]) and a[n1]!=' ':
        if a[n1]=='X':
            print('Вы победели!')
            return 1
        else:
            print('Вы проиграли')
            return 2
    return 0
     
    
def finish(a):
    return check(a,0,3,6)+check(a,1,4,7)+check(a,2,5,8)+check(a,0,1,2)+check(a,3,4,5)+check(a,6,7,8)+check(a,0,4,8)+check(a,2,4,6)


def smart(a):
    if smart_move(a,0,3,6) or smart_move(a,1,4,7) or smart_move(a,2,5,8) or smart_move(a,0,1,2) or smart_move(a,3,4,5) or smart_move(a,6,7,8) or smart_move(a,0,4,8) or smart_move(a,2,4,6):
        return 1
    else:
        return 0

def smart_move(a,n1,n2,n3):
    if ((a[n1]==a[n2]) and a[n1]=='X' and a[n3]==' '):
        a[n3]='O'
        return 1
    elif ((a[n1]==a[n3]) and a[n1]=='X' and a[n2]==' '):
        a[n2]='O'
        return 1
    elif ((a[n3]==a[n2]) and a[n1]=='X' and a[n1]==' '):
        a[n1]='O'
        return 1
    else:
        return 0

def win_move(a,n1,n2,n3):
    if ((a[n1]==a[n2]) and a[n1]=='O' and a[n3]==' '):
        a[n3]='O'
        return 1
    elif ((a[n1]==a[n3]) and a[n1]=='O' and a[n2]==' '):
        a[n2]='O'
        return 1
    elif ((a[n3]==a[n2]) and a[n1]=='O' and a[n1]==' '):
        a[n1]='O'
        return 1
    else:
        return 0

def win(a):
    if win_move(a,0,3,6) or win_move(a,1,4,7) or win_move(a,2,5,8) or win_move(a,0,1,2) or win_move(a,3,4,5) or win_move(a,6,7,8) or win_move(a,0,4,8) or win_move(a,2,4,6):
        return 1
    else:
        return 0

    
    

import random
game = [' ']*9
print_field(game)
while True:
    #мой ход
    w=inp()
    while w not in range(0,9):
        w=inp()
    while game[w]!=' ':
        print('Такой ход уже был!')
        w=inp()
    game[w]='X'
    print_field(game)

    if finish(game)!=0:
        break
    
    #компьютер

    print('ход компьютера:')
    if win(game)==1:
        print_field(game)
        print('Вы проиграли!')
        break
    if smart(game)==0:
        r=random.randint(0,8)
        while game[r]!=' ':
            r=random.randint(0,8)
        game[r]='O'
    print_field(game)

    if finish(game)!=0:
        break

