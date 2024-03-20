def check_sum(a,b,c):return a+b+c

def create_board(x_state,z_state):
    zero =  'x' if x_state[0]==1 else ('o' if z_state[0]==1 else 0)
    one =  'x' if x_state[1]==1 else ('o' if z_state[1]==1 else 1)
    two =  'x' if x_state[2]==1 else ('o' if z_state[2]==1 else 2)
    three =  'x' if x_state[3]==1 else ('o' if z_state[3]==1 else 3)
    four =  'x' if x_state[4]==1 else ('o' if z_state[4]==1 else 4)
    five =  'x' if x_state[5]==1 else ('o' if z_state[5]==1 else 5)
    six =  'x' if x_state[6]==1 else ('o' if z_state[6]==1 else 6)
    seven =  'x' if x_state[7]==1 else ('o' if z_state[7]==1 else 7)
    eight =  'x' if x_state[8]==1 else ('o' if z_state[8]==1 else 8)
    print(f'-------------')
    print(f'| {zero} | {one} | {two} |')
    print(f'-------------')
    print(f'| {three} | {four} | {five} |')
    print(f'-------------')
    print(f'| {six} | {seven} | {eight} |')
    print(f'-------------')
    print('\n\n')

def check_board(x_state,z_state):
    wins =[[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if (check_sum(x_state[win[0]],x_state[win[1]],x_state[win[2]])==3):
            print('X Won!!')
            return 1
        if (check_sum(z_state[win[0]],z_state[win[1]],z_state[win[2]])==3):
            print('O won!!')
            return 0
    return -1    


if __name__=='__main__':
    x_state=[0,0,0,0,0,0,0,0,0]
    z_state=[0,0,0,0,0,0,0,0,0]
    print('\n\nWelcome to tic tac toe\n')
    opt = input("\nEnter your choice (x ir o):")
    if opt=='x':turn=1
    else:turn=0
    while(True):
        create_board(x_state,z_state)
        if turn==1:
            val=int(input('X\'s turn: Enter a nunber:'))
            x_state[val]=1
            create_board(x_state,z_state)
        else:
            val=int(input('O\'s turn: Enter a nunber :'))
            z_state[val]=1
            create_board(x_state,z_state)

        win=check_board(x_state,z_state)
        if win!=-1:
            print('Match Over')
            break 

        turn = 1-turn      