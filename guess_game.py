print("\n")
print("This is a CLI program by vitriol...")
print("")


import random
import re


print ("")
print("this is a guessing game,you have [ 10 ] attempts")
print("this is version 6 of the game...")
print("")
print("CHANGE LOG".center(50,"-"))
print("")
print("game now has difficulty levels as you win...")
print('''users can now choose to play again or quit if they loose the game''')
print('''the maximum number is now set to 5 initially
so each level you win,the max is incremented by 2
the difficulty is then determined by the max number''')
print("other bug fixes...enjoy...")
print("")
print("")
print("[PLAY GAME BELOW]".center(50,"-"))
print ("")


'''set the maximum number and the minimum number
the failed variable is incremented each time 
a guess is wrong while the left variable is decremented
the game should end once the left vaiable hits zero
'''

maxx = 5
minn =1
failed_times = 0
left_attempts = 10
current_level=1


'''set variable to control game continuation'''

user_to_continue = False 

'''set master loop vriable (condition)'''

game_on = 1

while game_on == 1:

    '''create 4 random variables the guessed number 
    will be checked against,this makes the game easy.'''

    number1=random.randint(1,maxx)
    number2=random.randint(1,maxx)
    number3=random.randint(1,maxx)
    number4=random.randint(1,maxx)

    
    '''if the game was not ended,and user does not wanna
    continue'''
    
    if user_to_continue == False:

       '''create a variable to hold the entered guesses'''
       
       print("")
       guess=input("I THINK OF A NUMBER...\nGUESS THE NUMBER >> ")
       print("")
       '''the rest code are validations are conditions '''
       
       if re.search(r"\D",guess)  or guess=="":
          print('''please make sure to enter a number''')
          print("")
          
       else:
         if (int(guess) == number1 or
         	 int(guess) == number2 or
         	 int(guess) == number3 or
         	 int(guess) == number4):
         	 
           print("")
           print("")
           print("***************".center(50))
           print("CONGRATULATIONS".center(50))
           print("RIGHT GUESS".center(50))
           print("***************".center(50))
           print("")
           maxx+=2
           failed_times =0
           left_attempts =10
           current_level+=1
           
           print("LEVEL ", current_level ," ( max is now",maxx,")")
           game_on=1
           
         elif int(guess) > maxx:
           print ("your guess is a bit too high....")
           print("")
           
         elif int(guess) < minn: 
           print (" your guess is a little too low...")
           print("")
           
         elif failed_times == 10:
           print ("you have exhausted your chances without a win")
           print("")
           print ("*********".center(50))
           print ("GAME OVER".center(50))
           print("*********".center(50))
           print("")
           user_to_continue = True
           
         elif left_attempts==1:
           print("wrong guess, try again .. ")
           failed_times +=1
           left_attempts -=1
           print("this is your last attempt... ")
           print("")
           
         else:
           print("wrong guess, try again .. ")
           failed_times +=1
           left_attempts -=1
           print ("[ ",left_attempts," ] attempt(s) left..")
           print ("")
           
    elif user_to_continue == True:
    
        '''if game ended and user wanna continue...'''
        '''get reply from user '''
        
        print("\n")
        reply_prompt = input("WISH TO PLAY AGAIN ?  ")
        
        if reply_prompt in "Nn":
            print("")
            print("tanx for playing...")
            print("\n")
            print("GAME BY VITRIOL")
            game_on = 2
            
        elif reply_prompt in "Yy":
            left_attempts = 10 
            failed_times = 0
            user_to_continue = False
            
        else:
            print("")
            print("wrong input,please choose either (y,Y,N,n)")
            user_to_continue = True
            
    else:
        user_to_continue = False
            
            
        
        
       



##..code written by Vitriol...



#####