#intro

print("Hello, welcome to the basic general knowledge quiz:")

#asking to continue

cont=print("Do you want to continue?")

cont1=input("Press 'y' to continue and 'n' to continue: \n")

#If for continung

if cont1.upper() == "Y":
    print("Thanks for continuing,")

elif cont1.upper() == "N":
    print("You are exited successfully.")
    exit()

else:
    print("Sorry, I don't understand that.")
print("There will be 10 questions in this quiz")
print("Choose the correct option for the following questions")

#choosing the level

print("What level do you want?")

level=input("Press 'b' for begginer level, 'i' for intermediate, 'p' for pro level")

#if level if begginner

if level.upper() == "B":
    #questions for the quiz
    
    #ques1
    
    q1=print("What is the capital of India?")
    opt1=print("  a=New Delhi  \n  b=Kashmir  \n  c=Haryana  \n  d=Bihar")
    ans1=input("press the correct option: \n")
    
    #if for ques 1
    
    if ans1.upper() == "A": 
        print("Congrats, you got this answer correct")
    else:
        print("Sorry, your answer is not correct, try this next one")
    
    #ques 2
    
    q2=print("Who is the president of India?")
    opt2=print("  a=Narendra Modi  \n  b=Amit Shah  \n  c=Ram Nath Kovind  \n  d=Yogi Aditya Nath")
    ans2=input("press the correct option:\n")
    
    #if for ques 2
    
    if ans2.upper() == "C":
        print("Congrats you got this question correct.")
    else:
        print("Sorry, you get this question wrong.")
    
    #ques 3
    
    q3=print("How many states are there in India?")
    opt3=print("  a=20  \n  b=28  \n  c=29  \n  d=30")
    ans3=input("press the correct option: \n")
    
    #if for ques 3
    
    if ans3.upper() == "C":
        print("Congrats you got this question correct.")
    else:
        print("Sorry, you got this question wrong")
    
    #ques 4
    
    q4=print("In which year, India got independent?")
    opt4=print("  a=1898  \n  b=1999  \n  c=1900  \n  d=1947")
    ans4=input("press the correct option: \n")
    
    #if for ques 4
    
    if ans4.upper() == "D":
        print("Congrats you got this question correct.")
    else:
        print("Sorry, you got this question wrong")
    
    #ques 5
    
    q5=print("In which year, the indian constitution came into act?")
    opt5=print("  a=1947  \n  b=1999  \n  c=1950  \n  d=1949")
    ans5=input("press the correct option: \n")
    
    #if for ques 5
    
    if ans5.upper() == "C":
        print("Congrats you got this question correct.")
        exit()
    else:
        print("Sorry, you got this question wrong")
        exit()    

#if the level is intermediate

elif level.upper() == "I":
    print("You seems to be confident, let's start.")
    
    #ques 1
    
    qu1=print("Who is the home minister of India?")
    ch1=print("a=Nityanand Rai  \n  b=Ajay Kumar Mishra  \n  c=Amit Shah  \n  d=Indra Nooyi")
    an1=input("press the correct option: \n")
    
    #if for ques 1
    
    if an1.upper() == "C":
        print("Congrats you got this question correct.")
    else:
        print("Sorry,that's not the correct option")
    
    #ques 2
    
    qu2=print("Who is the defence minister of India?")
    ch2=print("  a=Nitin Gadkari  \n  b=Pankaj Singh  \n  c=Arun Jaitely  \n  d=Rajnath Singh")
    an2=input("Press the correct option:\n ")
    
    #if for ques 2
    
    if an2.upper() == "D":
        print("Congrats you got this question correct.")
    else:
        print("Sorry you got this question incorrect.")
    
    #ques 3
    
    qu3=print("When was the Indian constitution written?")
    ch3=print("  a=1950  \n  b=1947  \n  c=1949  \n  d=1990")
    an3=input("Press the correct option:\n ")
    
    #if for ques 3
    
    if an3.upper() == "C":
        print("Congrats you got this question correct.")
    else:
         print("Sorry you got this question incorrect.")
    
    #ques 4
    
    qu4=print("In which period of time, world war one took place?") 
    ch4=print("  a=1914-1918  \n  b=1913-1919  \n  c=1915-1920  \n  d=1916-1921")
    an4=input("Press the correct option:\n ")
    
    #if for ques 4
    
    if an4.upper() == "A":
        print("Congrats you got this question correct.")
    else:
        print("Sorry you got this question incorrect.")
    
    #ques 5

    qu5=print("When did the world war 2 took place?")
    ch5=print("  a=1939-1949  \n  b=1939-1944  \n  c=1939-1945  \n  d=1938-1945")
    an5=input("Press the correct option:\n ")
    
    #if for ques 5

    if an5.upper() == "C":
        print("Congrats you got this question correct.")
        exit()
    else:
        print("Sorry you got this question incorrect.")
        exit()

#if the level is pro

elif level.upper() == "P":
    print("So, you have chosen the pro level, this is not going to be easy.")
    print("So, here are the questions")
    
     #ques 1

    ques1=print("Who was the first scientist to win the noble prize?")
    choi=print("  a=Wilhelm Röntgen  \n  b=Albert Einstien  \n  c=Issac Newton  \n  d=Samue Colt")
    ra1=input("press the correct option: \n")
    
    #if for ques 1

    if ra1.upper() == "C":
        print("Congrats you got this question correct.")
    else:
        print("Sorry you got this question incorrect.")
    
    #ques 2
    ques2=print("Which cuntry gives the noble prize?")
    choi2=print("  a=Sweden  \n  b=Scotland  \n  c=Switzerland  \n  d=Singarpore")
    ra2=input("press the correct option: \n")
    
    #if for ques 2

    if ra2.upper() == "A":
        print("Congrats you got this question correct.")
    else:
        print("Sorry you got this question incorrect.")
    #ques 3

    ques3=print("Who was the first women president of India?")
    choi3=print("  a=Pratibha Patil  \n  b=Indra Gandhi  \n  c=Indra Nooyi  \n  d=None of the above")
    ra3=input("press the correct option: \n")
    
    #if for ques 3

    if ra3.upper() == "A":
        print("Congrats you got this question correct.")
    else:
        print("Sorry you got this question incorrect.")
    
    #ques 4
    
    ques4=print("Which is the largest river in India?")
    choi4=print("  a=Brahmputra  \n  b=Godavari  \n  c=Narmada  \n  d=Krishna")
    ra4=input("Press the correct option")
    
    #if for ques 4
    
    if ra4.upper() == "A":
        print("Congrats you got this question correct.")
    else:
        print("Sorry you got this question incorrect.")
    
    #ques 5
    
    ques5=print("Who was the first women governer of India?")
    choi5=print("  a=Sarojini Naidu  \n  b=Pratibha patil  \n  c=Sharda Mukherjee  \n  d=Vijaylaxmi Pandit")
    ra5=input("Press the correct option")
    
    # if for ques 5

    if ra5.upper() == "A":
        print("Congrats you got this question correct.")
        exit()
    else:
        print("Sorry you got this question incorrect.")
        exit()

#else statement

else:
    print("Sorry, I don't understand that.")

print("Come back for such projects")
