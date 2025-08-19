import random
list=["Rock","Paper","Scissor"]
random.choice(list)
while True:
    ucount=0
    ccount=0
    s=int (input('''
        1 Press 1 for Play...  
        2 Press 0 for Exit! 
        '''))
    print(" ")
    for i in range (1,6):
        if s==1:
            print("game start!....")
            user_input=int(input('''
            choose one of out these....
            1 Rock
            2 Paper
            3 Scissor
            
            '''))

            if user_input==1:
                userchoice="Rock"
            elif user_input==2:
                userchoice="Paper"
            elif user_input ==3:
                userchoice="Scissor"
            else:
                print("invalid choice")
            print(" ")
            print("your choice:-",userchoice)
            uc=userchoice
            comchoice=random.choice(list)
            
            print("computer's choice:-",comchoice)
            cc=comchoice
            
            if uc=="Rock" and cc=="Paper":
                print("computer win.")
                ccount+=1
            elif uc=="Rock" and cc=="Scissor":
                print("you win.")
                ucount+=1
            elif uc=="Paper" and cc=="Rock":
                print("you win.")
                ucount+=1
            elif uc=="Paper" and cc=="Scissor":
                print("computer win.")
                ccount+=1
            elif uc=="Scissor" and cc=="Paper":
                print("you win.")
                ucount+=1
            elif uc=="Scissor" and cc=="Rock":
                print("computer win.")
                ccount+=1
            else:
                ucount+=1
                ccount+=1
            print(" ")
            print("your score:- ",ucount)
            print("computer score:- ",ccount)
            if ucount>ccount:
                print("you won the Game.")
                print(" ")
            elif ucount< ccount:
                print("computer won the Game.")
                print(" ")
            elif ucount==ccount:
                print("Game Draw!.")
                print(" ")
        elif s==0:
            print("game over!..")
            break