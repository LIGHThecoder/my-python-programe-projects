
# date : 15/02/24
# Author : Nikhil Rajendra Gaikwad


#if ,elif, else , nested if statements

#creating a programe which shows student his 10th std records and also show him his futer plan in eductional carrier


#by using if ,elif, else , nested if statements



# how to print a lower case string to upper case?-------------
intro="--------------welcome to my few input and get future output programe.\nhope you will enjoy.--------------\n\n"
# print(intro.center())
print(intro.upper())


# print("enter your gender\n")
gender=int(input("enter your gender. if male then 1, if female than 2 and if third gender than 3\n"))
# print("the gender which you had chosen is",gender)


if(gender==1):
    print("you are male")

elif(gender==2):
    print("you are female")

elif(gender==3):
    print("you are in 3rd gender")











############################## male gender########################################################


if(gender==1):#######ok now boys turn 
    name=input("enter your name\n")
    roll=input("enter you 10th seat number\n")
    result=int(input("enter your 10th result\n"))

    if(result>=75):

        print("what you will chose after 10th.\nPRESS 1 FOR SCIENCE, 2 FOR ARTS, 3 FOR COMMERCE, 4 FOR DIPLOMA\n")
        stream=int(input("please enter you stream "))
        if(stream == 1):
             print("ok so you had choose SCIENCE as you stream after 10th\n what you are intrested in science press 1 for PCB, 2 for PCMB and 3 for NEET or JEE\n")
             sciencestream=int(input("enter you areas subject with the respect to the obove mentioned number\n"))

             if(sciencestream==1):
                print("ok so you had choose Physics, chemistry and biology as you subject in science")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")

             elif(sciencestream==2):
                print("ok so you had choose Physics, chemistry, maths and biology as you subject in science")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")

             elif(sciencestream==3):
                print("ok so you are planning to do JEE or NEET in science")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")


            

        elif(stream==2):
    #         name=input("enter your name\n")
    #         roll=input("enter you 10th seat number\n")
    #         result=int(input("enter your 10th result\n"))
    
    # if(result>=75):
    #     print("what you will chose after 10th.\nPRESS 1 FOR SCIENCE, 2 FOR ARTS, 3 FOR COMMERCE, 4 FOR DIPLOMA\n")
    #     stream=int(input("please enter you stream "))
    #     if(stream == 2):
            print("ok so you had choose ARTS as you stream after 10th\n what you are intrested in arts press 1 for literature, 2 for government exams and 3 for history learning")
            sciencestream=int(input("enter you areas subject with the respect to the obove mentioned number\n"))

            if(sciencestream==1):
                print("ok so you had choose literature as you subject in ARTS")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")

            elif(sciencestream==2):
                print("ok so you had aimed for goverment exam so that's the reason  ARTS")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")

            elif(sciencestream==3):
                print("ok so you are planning to learn history lerning in ARTS")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")



        elif(stream==3):
             print("ok so you had choose COMMERECE as you stream after 10th\n what you are intrested in COMMERECE press 1 for banking, 2 for CA and 3 for going on the road of MBA ")

             sciencestream=int(input("enter you areas subject with the respect to the obove mentioned number\n"))
            
             if(sciencestream==1):
                print("ok so you had choose banking as you subject in COMMERECE")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")

             elif(sciencestream==2):
                print("ok so you had aimed CA exam so that's the reason  COMMERECE")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")

             elif(sciencestream==3):
                print("ok so you are going on the road of MBA in COMMERECE")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")


        elif(stream==4):
              print("ok so you had choose DIPLOMA as you stream after 10th\n what you are intrested in DIPLOMA press 1 for engineering diploma, 2 for Hotel management")
              sciencestream=int(input("enter you areas subject with the respect to the obove mentioned number\n"))

              if(sciencestream==1):
                print("ok so you had choose engineering diploma as you subject in DIPLOMA")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")

              elif(sciencestream==2):
                print("ok so you had choose Hotel Management as you subject in DIPLOMA")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")

            #   elif(sciencestream==3):
            #     print("ok so you are planning to do JEE or NEET in DIPLOMA")

#################################################################################################
        
    elif(result<=74 and result>=60):
        print("how many stars would you like to give to your 10th performance outof 3 ")
        star=int(input("ente how mnay stars will you give to your self outof 3"))
        print("you had give",star," stars to your performace\n")


        print("what you will chose after 10th.\nPRESS 1 FOR SCIENCE, 2 FOR ARTS, 3 FOR COMMERCE, 4 FOR DIPLOMA\n")
        stream=int(input("please enter you stream "))
        if(stream == 1):
            print("ok so you had choose SCIENCE as you stream after 10th\n what you are intrested in science press 1 for PCB, 2 for PCMB and 3 for NEET or JEE")
            sciencestream=int(input("enter you areas subject with the respect to the obove mentioned number\n"))
            if(sciencestream==1):
                print("ok so you had choose Physics, chemistry and biology as you subject in science")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")

            elif(sciencestream==2):
                print("ok so you had choose Physics, chemistry, maths and biology as you subject in science")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")

            elif(sciencestream==3):
                print("ok so you are planning to do JEE or NEET in science")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")



            

        elif(stream==2):
    #         name=input("enter your name\n")
    #         roll=input("enter you 10th seat number\n")
    #         result=int(input("enter your 10th result\n"))
    
    # if(stream == 2):
    #     print("what you will chose after 10th.\nPRESS 1 FOR SCIENCE, 2 FOR ARTS, 3 FOR COMMERCE, 4 FOR DIPLOMA\n")
    #     stream=int(input("please enter you stream "))
    #     if(stream == 2):
            print("ok so you had choose ARTS as you stream after 10th\n what you are intrested in arts press 1 for literature, 2 for government exams and 3 for history learning")
            sciencestream=int(input("enter you areas subject with the respect to the obove mentioned number\n"))
            if(sciencestream==1):
                print("ok so you had choose literature as you subject in ARTS")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")

            elif(sciencestream==2):
                print("ok so you had aimed for goverment exam so that's the reason  ARTS")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")

            elif(sciencestream==3):
                print("ok so you are planning to learn history lerning in ARTS")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")



        elif(stream==3):
             print("ok so you had choose COMMERECE as you stream after 10th\n what you are intrested in COMMERECE press 1 for banking, 2 for CA and 3 for going on the road of MBA ")
             sciencestream=int(input("enter you areas subject with the respect to the obove mentioned number\n"))
             if(sciencestream==1):
                print("ok so you had choose banking as you subject in COMMERECE")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")

             elif(sciencestream==2):
                print("ok so you had aimed CA exam so that's the reason  COMMERECE")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")

             elif(sciencestream==3):
                print("ok so you are going on the road of MBA in COMMERECE")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")


        elif(stream==4):
              print("ok so you had choose DIPLOMA as you stream after 10th\n what you are intrested in DIPLOMA press 1 for engineering diploma, 2 for Hotel management")
              sciencestream=int(input("enter you areas subject with the respect to the obove mentioned number\n"))
              if(sciencestream==1):
                print("ok so you had choose engineering diploma as you subject in DIPLOMA")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")

              elif(sciencestream==2):
                print("ok so you had choose Hotel Management as you subject in DIPLOMA")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")

            #   elif(sciencestream==3):
            #     print("ok so you are planning to do JEE or NEET in DIPLOMA")
    
    ################################################################################################


    elif(result>60):
        print("you must be not happy with your Percentage but let me tell you one thing this is not end you will improve\n")
        print("how many stars would you like to give to your 10th performance outof 3 ")
        star=int(input("ente how mnay stars will you give to your self outof 3"))
        print("you had give",star," stars to your performace\n")


        print("what you will chose after 10th.\nPRESS 1 FOR SCIENCE, 2 FOR ARTS, 3 FOR COMMERCE, 4 FOR DIPLOMA\n")
        stream=int(input("please enter you stream "))
        if(stream == 1):
            print("ok so you had choose SCIENCE as you stream after 10th\n what you are intrested in science press 1 for PCB, 2 for PCMB and 3 for NEET or JEE")
            sciencestream=int(input("enter you areas subject with the respect to the obove mentioned number\n"))
            if(sciencestream==1):
                print("ok so you had choose Physics, chemistry and biology as you subject in science")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")

            elif(sciencestream==2):
                print("ok so you had choose Physics, chemistry, maths and biology as you subject in science")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")

            elif(sciencestream==3):
                print("ok so you are planning to do JEE or NEET in science")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")



            

        elif(stream==2):
    #         name=input("enter your name\n")
    #         roll=input("enter you 10th seat number\n")
    #         result=int(input("enter your 10th result\n"))
    
    # if(result>=75):
    #     print("what you will chose after 10th.\nPRESS 1 FOR SCIENCE, 2 FOR ARTS, 3 FOR COMMERCE, 4 FOR DIPLOMA\n")
    #     stream=int(input("please enter you stream "))
    #     if(stream == 2):
            print("ok so you had choose ARTS as you stream after 10th\n what you are intrested in arts press 1 for literature, 2 for government exams and 3 for history learning")
            sciencestream=int(input("enter you areas subject with the respect to the obove mentioned number\n"))
            if(sciencestream==1):
                print("ok so you had choose literature as you subject in ARTS")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")

            elif(sciencestream==2):
                print("ok so you had aimed for goverment exam so that's the reason  ARTS")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")

            elif(sciencestream==3):
                print("ok so you are planning to learn history lerning in ARTS")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")



        elif(stream==3):
             print("ok so you had choose COMMERECE as you stream after 10th\n what you are intrested in COMMERECE press 1 for banking, 2 for CA and 3 for going on the road of MBA ")
             sciencestream=int(input("enter you areas subject with the respect to the obove mentioned number\n"))
             if(sciencestream==1):
                print("ok so you had choose banking as you subject in COMMERECE")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")

             elif(sciencestream==2):
                print("ok so you had aimed CA exam so that's the reason  COMMERECE")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")

             elif(sciencestream==3):
                print("ok so you are going on the road of MBA in COMMERECE")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")


        elif(stream==4):
              print("ok so you had choose DIPLOMA as you stream after 10th\n what you are intrested in DIPLOMA press 1 for engineering diploma, 2 for Hotel management")
              sciencestream=int(input("enter you areas subject with the respect to the obove mentioned number\n"))
              if(sciencestream==1):
                print("ok so you had choose engineering diploma as you subject in DIPLOMA")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")

              elif(sciencestream==2):
                print("ok so you had choose Hotel Management as you subject in DIPLOMA")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")

            #   elif(sciencestream==3):
            #     print("ok so you are planning to do JEE or NEET in DIPLOMA")












##############################female gender########################################################












elif(gender==2):# now girls turn
    name=input("enter your name\n")
    roll=input("enter you 10th seat number\n")
    result=int(input("enter your 10th result\n"))

    if(result>=75):

        print("what you will chose after 10th.\nPRESS 1 FOR SCIENCE, 2 FOR ARTS, 3 FOR COMMERCE, 4 FOR DIPLOMA\n")
        stream=int(input("please enter you stream "))
        if(stream == 1):
            print("ok so you had choose SCIENCE as you stream after 10th\n what you are intrested in science press 1 for PCB, 2 for PCMB and 3 for NEET or JEE")
            sciencestream=int(input("enter you areas subject with the respect to the obove mentioned number\n"))
            if(sciencestream==1):
                print("ok so you had choose Physics, chemistry and biology as you subject in science")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")

            elif(sciencestream==2):
                print("ok so you had choose Physics, chemistry, maths and biology as you subject in science")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")

            elif(sciencestream==3):
                print("ok so you are planning to do JEE or NEET in science")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")



            

        elif(stream==2):
    #         name=input("enter your name\n")
    #         roll=input("enter you 10th seat number\n")
    #         result=int(input("enter your 10th result\n"))
    
    # if(result>=75):
    #     print("what you will chose after 10th.\nPRESS 1 FOR SCIENCE, 2 FOR ARTS, 3 FOR COMMERCE, 4 FOR DIPLOMA\n")
    #     stream=int(input("please enter you stream "))
    #     if(stream == 2):
            print("ok so you had choose ARTS as you stream after 10th\n what you are intrested in arts press 1 for literature, 2 for government exams and 3 for history learning")
            sciencestream=int(input("enter you areas subject with the respect to the obove mentioned number\n"))
            if(sciencestream==1):
                print("ok so you had choose literature as you subject in ARTS")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")

            elif(sciencestream==2):
                print("ok so you had aimed for goverment exam so that's the reason  ARTS")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")

            elif(sciencestream==3):
                print("ok so you are planning to learn history lerning in ARTS")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")

                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")



        elif(stream==3):
             print("ok so you had choose COMMERECE as you stream after 10th\n what you are intrested in COMMERECE press 1 for banking, 2 for CA and 3 for going on the road of MBA ")
             sciencestream=int(input("enter you areas subject with the respect to the obove mentioned number\n"))
             if(sciencestream==1):
                print("ok so you had choose banking as you subject in COMMERECE")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")

             elif(sciencestream==2):
                print("ok so you had aimed CA exam so that's the reason  COMMERECE")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")

             elif(sciencestream==3):
                print("ok so you are going on the road of MBA in COMMERECE")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")


        elif(stream==4):
              print("ok so you had choose DIPLOMA as you stream after 10th\n what you are intrested in DIPLOMA press 1 for engineering diploma, 2 for Hotel management")
              sciencestream=int(input("enter you areas subject with the respect to the obove mentioned number\n"))
              if(sciencestream==1):
                print("ok so you had choose engineering diploma as you subject in DIPLOMA")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")
                
              elif(sciencestream==2):
                print("ok so you had choose Hotel Management as you subject in DIPLOMA")
                
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")

            #   elif(sciencestream==3):
            #     print("ok so you are planning to do JEE or NEET in DIPLOMA")

#################################################################################################
        
    elif(result<=74 and result>=60):
        print("how many stars would you like to give to your 10th performance outof 3 ")
        star=int(input("ente how mnay stars will you give to your self outof 3"))
        print("you had give",star," stars to your performace\n")


        print("what you will chose after 10th.\nPRESS 1 FOR SCIENCE, 2 FOR ARTS, 3 FOR COMMERCE, 4 FOR DIPLOMA\n")
        stream=int(input("please enter you stream "))
        if(stream == 1):
            print("ok so you had choose SCIENCE as you stream after 10th\n what you are intrested in science press 1 for PCB, 2 for PCMB and 3 for NEET or JEE")
            sciencestream=int(input("enter you areas subject with the respect to the obove mentioned number\n"))
            if(sciencestream==1):
                print("ok so you had choose Physics, chemistry and biology as you subject in science")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")

            elif(sciencestream==2):
                print("ok so you had choose Physics, chemistry, maths and biology as you subject in science")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")

            elif(sciencestream==3):
                print("ok so you are planning to do JEE or NEET in science")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")



            

        elif(stream==2):
    #         name=input("enter your name\n")
    #         roll=input("enter you 10th seat number\n")
    #         result=int(input("enter your 10th result\n"))
    
    # if(stream == 2):
    #     print("what you will chose after 10th.\nPRESS 1 FOR SCIENCE, 2 FOR ARTS, 3 FOR COMMERCE, 4 FOR DIPLOMA\n")
    #     stream=int(input("please enter you stream "))
    #     if(stream == 2):
            print("ok so you had choose ARTS as you stream after 10th\n what you are intrested in arts press 1 for literature, 2 for government exams and 3 for history learning")
            sciencestream=int(input("enter you areas subject with the respect to the obove mentioned number\n"))
            if(sciencestream==1):
                print("ok so you had choose literature as you subject in ARTS")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")

            elif(sciencestream==2):
                print("ok so you had aimed for goverment exam so that's the reason  ARTS")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")

            elif(sciencestream==3):
                print("ok so you are planning to learn history lerning in ARTS")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")



        elif(stream==3):
             print("ok so you had choose COMMERECE as you stream after 10th\n what you are intrested in COMMERECE press 1 for banking, 2 for CA and 3 for going on the road of MBA ")
             sciencestream=int(input("enter you areas subject with the respect to the obove mentioned number\n"))
             if(sciencestream==1):
                print("ok so you had choose banking as you subject in COMMERECE")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")

             elif(sciencestream==2):
                print("ok so you had aimed CA exam so that's the reason  COMMERECE")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")

             elif(sciencestream==3):
                print("ok so you are going on the road of MBA in COMMERECE")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")


        elif(stream==4):
              print("ok so you had choose DIPLOMA as you stream after 10th\n what you are intrested in DIPLOMA press 1 for engineering diploma, 2 for Hotel management")
              sciencestream=int(input("enter you areas subject with the respect to the obove mentioned number\n"))
              if(sciencestream==1):
                print("ok so you had choose engineering diploma as you subject in DIPLOMA")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")

              elif(sciencestream==2):
                print("ok so you had choose Hotel Management as you subject in DIPLOMA")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")

            #   elif(sciencestream==3):
            #     print("ok so you are planning to do JEE or NEET in DIPLOMA")
    
    ################################################################################################

    
    elif(result>60):
        print("you must be not happy with your Percentage but let me tell you one thing this is not end you will improve\n")
        print("how many stars would you like to give to your 10th performance outof 3 ")
        star=int(input("ente how mnay stars will you give to your self outof 3"))
        print("you had give",star," stars to your performace\n")


        print("what you will chose after 10th.\nPRESS 1 FOR SCIENCE, 2 FOR ARTS, 3 FOR COMMERCE, 4 FOR DIPLOMA\n")
        stream=int(input("please enter you stream "))
        if(stream == 1):
            print("ok so you had choose SCIENCE as you stream after 10th\n what you are intrested in science press 1 for PCB, 2 for PCMB and 3 for NEET or JEE")
            sciencestream=int(input("enter you areas subject with the respect to the obove mentioned number\n"))
            if(sciencestream==1):
                print("ok so you had choose Physics, chemistry and biology as you subject in science")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")

            elif(sciencestream==2):
                print("ok so you had choose Physics, chemistry, maths and biology as you subject in science")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")

            elif(sciencestream==3):
                print("ok so you are planning to do JEE or NEET in science")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")



            

        elif(stream==2):
    #         name=input("enter your name\n")
    #         roll=input("enter you 10th seat number\n")
    #         result=int(input("enter your 10th result\n"))
    
    # if(result>=75):
    #     print("what you will chose after 10th.\nPRESS 1 FOR SCIENCE, 2 FOR ARTS, 3 FOR COMMERCE, 4 FOR DIPLOMA\n")
    #     stream=int(input("please enter you stream "))
    #     if(stream == 2):
            print("ok so you had choose ARTS as you stream after 10th\n what you are intrested in arts press 1 for literature, 2 for government exams and 3 for history learning")
            sciencestream=int(input("enter you areas subject with the respect to the obove mentioned number\n"))
            if(sciencestream==1):
                print("ok so you had choose literature as you subject in ARTS")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")

            elif(sciencestream==2):
                print("ok so you had aimed for goverment exam so that's the reason  ARTS")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")

            elif(sciencestream==3):
                print("ok so you are planning to learn history lerning in ARTS")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")



        elif(stream==3):
             print("ok so you had choose COMMERECE as you stream after 10th\n what you are intrested in COMMERECE press 1 for banking, 2 for CA and 3 for going on the road of MBA ")
             sciencestream=int(input("enter you areas subject with the respect to the obove mentioned number\n"))
             if(sciencestream==1):
                print("ok so you had choose banking as you subject in COMMERECE")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")

             elif(sciencestream==2):
                print("ok so you had aimed CA exam so that's the reason  COMMERECE")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")

             elif(sciencestream==3):
                print("ok so you are going on the road of MBA in COMMERECE")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")


        elif(stream==4):
              print("ok so you had choose DIPLOMA as you stream after 10th\n what you are intrested in DIPLOMA press 1 for engineering diploma, 2 for Hotel management")
              sciencestream=int(input("enter you areas subject with the respect to the obove mentioned number\n"))
              if(sciencestream==1):
                print("ok so you had choose engineering diploma as you subject in DIPLOMA")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")

              elif(sciencestream==2):
                print("ok so you had choose Hotel Management as you subject in DIPLOMA")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")

            #   elif(sciencestream==3):
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")

            #     print("ok so you are planning to do JEE or NEET in DIPLOMA")

    


    ################################################################################################




















##############################third gender########################################################




elif(gender==3): # now third gender turn
    name=input("enter your name\n")
    roll=input("enter you 10th seat number\n")
    result=int(input("enter your 10th result\n"))

    if(result>=75):

        print("what you will chose after 10th.\nPRESS 1 FOR SCIENCE, 2 FOR ARTS, 3 FOR COMMERCE, 4 FOR DIPLOMA\n")
        stream=int(input("please enter you stream "))
        if(stream == 1):
            print("ok so you had choose SCIENCE as you stream after 10th\n what you are intrested in science press 1 for PCB, 2 for PCMB and 3 for NEET or JEE")
            sciencestream=int(input("enter you areas subject with the respect to the obove mentioned number\n"))
            if(sciencestream==1):
                print("ok so you had choose Physics, chemistry and biology as you subject in science")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")

            elif(sciencestream==2):
                print("ok so you had choose Physics, chemistry, maths and biology as you subject in science")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")

            elif(sciencestream==3):
                print("ok so you are planning to do JEE or NEET in science")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")



            

        elif(stream==2):
    #         name=input("enter your name\n")
    #         roll=input("enter you 10th seat number\n")
    #         result=int(input("enter your 10th result\n"))
    
    # if(result>=75):
    #     print("what you will chose after 10th.\nPRESS 1 FOR SCIENCE, 2 FOR ARTS, 3 FOR COMMERCE, 4 FOR DIPLOMA\n")
    #     stream=int(input("please enter you stream "))
    #     if(stream == 2):
            print("ok so you had choose ARTS as you stream after 10th\n what you are intrested in arts press 1 for literature, 2 for government exams and 3 for history learning")
            sciencestream=int(input("enter you areas subject with the respect to the obove mentioned number\n"))
            if(sciencestream==1):
                print("ok so you had choose literature as you subject in ARTS")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")

            elif(sciencestream==2):
                print("ok so you had aimed for goverment exam so that's the reason  ARTS")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")

            elif(sciencestream==3):
                print("ok so you are planning to learn history lerning in ARTS")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")



        elif(stream==3):
             print("ok so you had choose COMMERECE as you stream after 10th\n what you are intrested in COMMERECE press 1 for banking, 2 for CA and 3 for going on the road of MBA ")
             sciencestream=int(input("enter you areas subject with the respect to the obove mentioned number\n"))
             if(sciencestream==1):
                print("ok so you had choose banking as you subject in COMMERECE")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")

             elif(sciencestream==2):
                print("ok so you had aimed CA exam so that's the reason  COMMERECE")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")

             elif(sciencestream==3):
                print("ok so you are going on the road of MBA in COMMERECE")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")


        elif(stream==4):
              print("ok so you had choose DIPLOMA as you stream after 10th\n what you are intrested in DIPLOMA press 1 for engineering diploma, 2 for Hotel management")
              sciencestream=int(input("enter you areas subject with the respect to the obove mentioned number\n"))
              if(sciencestream==1):
                print("ok so you had choose engineering diploma as you subject in DIPLOMA")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")

              elif(sciencestream==2):
                print("ok so you had choose Hotel Management as you subject in DIPLOMA")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")

            #   elif(sciencestream==3):
            #     print("ok so you are planning to do JEE or NEET in DIPLOMA")

#################################################################################################
        
    elif(result<=74 and result>=60):
        print("how many stars would you like to give to your 10th performance outof 3 ")
        star=int(input("ente how mnay stars will you give to your self outof 3"))
        print("you had give",star," stars to your performace\n")


        print("what you will chose after 10th.\nPRESS 1 FOR SCIENCE, 2 FOR ARTS, 3 FOR COMMERCE, 4 FOR DIPLOMA\n")
        stream=int(input("please enter you stream "))
        if(stream == 1):
            print("ok so you had choose SCIENCE as you stream after 10th\n what you are intrested in science press 1 for PCB, 2 for PCMB and 3 for NEET or JEE")
            sciencestream=int(input("enter you areas subject with the respect to the obove mentioned number\n"))
            if(sciencestream==1):
                print("ok so you had choose Physics, chemistry and biology as you subject in science")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")

            elif(sciencestream==2):
                print("ok so you had choose Physics, chemistry, maths and biology as you subject in science")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")

            elif(sciencestream==3):
                print("ok so you are planning to do JEE or NEET in science")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")



            

        elif(stream==2):
    #         name=input("enter your name\n")
    #         roll=input("enter you 10th seat number\n")
    #         result=int(input("enter your 10th result\n"))
    
    # if(stream == 2):
    #     print("what you will chose after 10th.\nPRESS 1 FOR SCIENCE, 2 FOR ARTS, 3 FOR COMMERCE, 4 FOR DIPLOMA\n")
    #     stream=int(input("please enter you stream "))
    #     if(stream == 2):
            print("ok so you had choose ARTS as you stream after 10th\n what you are intrested in arts press 1 for literature, 2 for government exams and 3 for history learning")
            sciencestream=int(input("enter you areas subject with the respect to the obove mentioned number\n"))
            if(sciencestream==1):
                print("ok so you had choose literature as you subject in ARTS")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")

            elif(sciencestream==2):
                print("ok so you had aimed for goverment exam so that's the reason  ARTS")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")

            elif(sciencestream==3):
                print("ok so you are planning to learn history lerning in ARTS")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")



        elif(stream==3):
             print("ok so you had choose COMMERECE as you stream after 10th\n what you are intrested in COMMERECE press 1 for banking, 2 for CA and 3 for going on the road of MBA ")
             sciencestream=int(input("enter you areas subject with the respect to the obove mentioned number\n"))
             if(sciencestream==1):
                print("ok so you had choose banking as you subject in COMMERECE")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")

             elif(sciencestream==2):
                print("ok so you had aimed CA exam so that's the reason  COMMERECE")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")

             elif(sciencestream==3):
                print("ok so you are going on the road of MBA in COMMERECE")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")


        elif(stream==4):
              print("ok so you had choose DIPLOMA as you stream after 10th\n what you are intrested in DIPLOMA press 1 for engineering diploma, 2 for Hotel management")
              sciencestream=int(input("enter you areas subject with the respect to the obove mentioned number\n"))
              if(sciencestream==1):
                print("ok so you had choose engineering diploma as you subject in DIPLOMA")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")

              elif(sciencestream==2):
                print("ok so you had choose Hotel Management as you subject in DIPLOMA")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")

            #   elif(sciencestream==3):
            #     print("ok so you are planning to do JEE or NEET in DIPLOMA")
    
    ################################################################################################

    
    elif(result>60):
        print("you must be not happy with your Percentage but let me tell you one thing this is not end you will improve\n")
        print("how many stars would you like to give to your 10th performance outof 3 ")
        star=int(input("ente how mnay stars will you give to your self outof 3"))
        print("you had give",star," stars to your performace\n")


        print("what you will chose after 10th.\nPRESS 1 FOR SCIENCE, 2 FOR ARTS, 3 FOR COMMERCE, 4 FOR DIPLOMA\n")
        stream=int(input("please enter you stream "))
        if(stream == 1):
            print("ok so you had choose SCIENCE as you stream after 10th\n what you are intrested in science press 1 for PCB, 2 for PCMB and 3 for NEET or JEE")
            sciencestream=int(input("enter you areas subject with the respect to the obove mentioned number\n"))
            if(sciencestream==1):
                print("ok so you had choose Physics, chemistry and biology as you subject in science")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")

            elif(sciencestream==2):
                print("ok so you had choose Physics, chemistry, maths and biology as you subject in science")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")

            elif(sciencestream==3):
                print("ok so you are planning to do JEE or NEET in science")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")



            

        elif(stream==2):
    #         name=input("enter your name\n")
    #         roll=input("enter you 10th seat number\n")
    #         result=int(input("enter your 10th result\n"))
    
    # if(result>=75):
    #     print("what you will chose after 10th.\nPRESS 1 FOR SCIENCE, 2 FOR ARTS, 3 FOR COMMERCE, 4 FOR DIPLOMA\n")
    #     stream=int(input("please enter you stream "))
    #     if(stream == 2):
            print("ok so you had choose ARTS as you stream after 10th\n what you are intrested in arts press 1 for literature, 2 for government exams and 3 for history learning")
            sciencestream=int(input("enter you areas subject with the respect to the obove mentioned number\n"))
            if(sciencestream==1):
                print("ok so you had choose literature as you subject in ARTS")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")

            elif(sciencestream==2):
                print("ok so you had aimed for goverment exam so that's the reason  ARTS")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")

            elif(sciencestream==3):
                print("ok so you are planning to learn history lerning in ARTS")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")



        elif(stream==3):
             print("ok so you had choose COMMERECE as you stream after 10th\n what you are intrested in COMMERECE press 1 for banking, 2 for CA and 3 for going on the road of MBA ")
             sciencestream=int(input("enter you areas subject with the respect to the obove mentioned number\n"))
             if(sciencestream==1):
                print("ok so you had choose banking as you subject in COMMERECE")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")

             elif(sciencestream==2):
                print("ok so you had aimed CA exam so that's the reason  COMMERECE")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")

             elif(sciencestream==3):
                print("ok so you are going on the road of MBA in COMMERECE")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")


        elif(stream==4):
              print("ok so you had choose DIPLOMA as you stream after 10th\n what you are intrested in DIPLOMA press 1 for engineering diploma, 2 for Hotel management")
              sciencestream=int(input("enter you areas subject with the respect to the obove mentioned number\n"))
              if(sciencestream==1):
                print("ok so you had choose engineering diploma as you subject in DIPLOMA")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")

              elif(sciencestream==2):
                print("ok so you had choose Hotel Management as you subject in DIPLOMA")
                print("that's for it from my side I hope that i had given you, your educational past as well as future plans.\nALL THE BEST FOR YOUR BRIGHT FUTURE")

            #   elif(sciencestream==3):
            #     print("ok so you are planning to do JEE or NEET in DIPLOMA")




###############################################################################################################33







