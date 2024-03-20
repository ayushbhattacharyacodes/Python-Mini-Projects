import random,os

def start_game():
        words=["apple","banana","orange","dragonfruit","mangoes","grapes"]
        word=random.choice(words)
        box=["-" for _ in range(len(word))]
        create_blank(box)
        return box,word

def create_blank(box):
      for i in box:
            print(f'{i}',end=' ')
      print("\n")      

def guess_word(word,letter,box,chance):
      wrong=0
      for idx,w in enumerate(word):
        if letter==w:
            box[idx]=letter
        if letter!=w:
             wrong+=1
      if wrong==len(word):
              print("Oops!! You guessed it wrong.. Try again\n")
              chance-=1
              print(f'You have {chance} chances left!!\n\n')     
      create_blank(box)
      return box,chance                 
      

if __name__=='__main__':
        alpha,chance,option=6,'y',[]
        print("\nWelcome!! Let\'s play Hangman\n")
        print("\nYou have 6 chances to guess a word\n")
        box,word=start_game()
        while option!='n':
                letter=input("Enter a letter to guess: ").lower()
                if letter in alpha:
                    print("\nLetter already used!!")
                    letter=input("Enter another letter to guess: ").lower()
                else:
                    alpha.append(letter) 
                res,chance=guess_word(word,letter,box,chance)
                if word==''.join(res) :
                    print('Congrats!! You guessed the word')
                    print(f'The word is {word}') 
                    option=input("Do you wish to play again?? (y/n): ")
                    if option=='y':
                      start_game()
                      os.system('cls')
                      create_blank(box)  
                elif chance==0:
                    print('\nGame Over!!')
                    print(f'\nThe word was {word}\n')
                    break
       