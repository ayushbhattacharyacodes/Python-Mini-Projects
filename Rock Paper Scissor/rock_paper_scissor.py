import os

def match_option(c1,c2,li):
     s1,s2=li
     if c1==c2:
        s1+=0
        s2+=0
        print(f'\n\nNo points')
     else:   
        if c1=='r':
            if c2=='p':
                s1+=0
                s2+=1
                print('\n\nPaper Wins\nPlayer 2 gets a point')
            elif c2=='s':
                 s1+=1
                 s2+=0
                 print('\n\nScissor Wins\nPlayer 1 gets a point')
        elif c1=='p':          
            if c2=='r':
                s1+=1
                s2+=0
                print('\n\nPaper Wins\nPlayer 1 gets a point')
            elif c2=='s':
                s1+=0
                s2+=1
                print('\n\nScissor Wins\nPlayer 2 gets a point')
        elif c1=='s':          
            if c2=='r':
                s1+=0
                s2+=1
                print('\n\nRock Wins\nPlayer 2 gets a point')
            elif c2=='p':
                s1+=1
                s2+=0
                print('\n\nPaper Wins\nPlayer 1 gets a point')

     print(f'\nScore \nPlayer 1 gets {s1} points \nPlayer 2 gets {s2} points\n\n')
     
     return [s1,s2]       

def display_results(li):
    r1,r2=li
    if r1>r2:
        print('\nPlayer 1 Won')
    elif r1<r2:
        print('\nPlayer 2 Won')
    else:
        print('\nIt\'s a tie')
    return                   

if __name__=='__main__':
    print("Lets play Rock Paper Scissors!!\n")
    choice = 'y'
    scores_list=[0,0]
    while(choice!='n'):
        p1=input("Player 1 goes first \n Rock(r)\n Paper(p)\n Scissor(s)\nEnter Your Choice:  ")
        os.system('cls')
        p2=input("Player 2 goes next \n Rock(r)\n Paper(p)\n Scissor(s)\nEnter Your Choice:  ")
        result_list=match_option(p1,p2,scores_list)
        choice = input('Would you like to Continue(y/n): ')
        if choice=='y':
            os.system('cls')

    display_results(result_list)       