"""---------day 26 or video 26-----------


Author : NIKHIL RAJENDRA GAIKWAD

topic name : kon banega karod pathi in python (KBC)

date:28/02/24



"""

# print("xx")
"""
 I REVEAL WE HAVE TO USE FUNCTION TO MAKE THIS PROGRAM QUESTION 10
create a programe capable of displaying questions to the user like KBC.

use list datatype to store the questions and their correct answers.

display the final amount the person is taking home after playing the game.


"""

b = ("--------welcome to NRG's KBC--------")
print(b.center(50))
print("\n")
print("rules of the game are as follows:")
print("1.there will be 10 questions in total")
print("2.there will be 1 question at a time and you will have 4 option for it")
print(
    "3.as you win the question the money amount given to you will also increased"
)
money = ("4.it will start from 10 lakhs till 1 CR")
print("\n")
print("IF YOU WANT TO CLICK ON OPTION A CLICK ON 1")
print("IF YOU WANT TO CLICK ON OPTION B CLICK ON 2")
print("IF YOU WANT TO CLICK ON OPTION C CLICK ON 3")
print("IF YOU WANT TO CLICK ON OPTION D CLICK ON 4")
print("\n")
print(money.title())
print("\n")
a = ("All the best hope you get a big money home!!!")
print(a.title())
print("\n")

#------------------------making function-----------------------------------------

# def KBC(a,b,c,d):

#------------------------making function-----------------------------------------

# ------------------------question 1 workplace------------------
quetion1 = ["what is real name of Iron man?"]
options1 = ["steve", "tony", "peter", "tony stark"]
print(quetion1)
print("you options are", options1)
correct_answer = int(input("enter your answer's option as per the rule\n"))

if correct_answer == 1:
  print("sorry you have selected wrong answer")
  print(
      "sorry to say but option a is wrong answer sorry but you will go empty had"
  )

elif (correct_answer == 2):
  print("sorry you have selected wrong answer")
  print(
      "sorry to say but option b is wrong answer sorry but you will go empty hand"
  )

elif (correct_answer == 3):
  print("sorry you have selected wrong answer")
  print(
      "sorry to say but option c is wrong answer sorry but you will go empty had"
  )

elif (correct_answer == 4):
  print("CONGRATULATION YOU HAVE SELECTED CORRECT OPTION")
  won1 = ("you have won 10 lakhs!!!!!!!!!!!!!!!")
  print(won1.title())
  print("\n")
  print("now get ready for next question all the best")
  #-----------------question 2 workplace---------------
  question2 = ["Ash's first pokemon"]
  print(question2)
  option2 = ["1.pikachu", "2.bulbasaur", "3.charmander", "4.squirt"]
  print(option2)
  correct_answer2 = int(input("enter your answer's option as per the rule\n"))
  if correct_answer2 == 1:
    print("CONGRATULATION YOU HAVE SELECTED CORRECT OPTION")
    print("you have won 20 lakhs!!!!!!!!!!!!!!!")
    print("get ready for the next question")
    print("\n")
    #-----------------question 3 workplace---------------
    question3 = ["who is the king of the jungle?"]
    print(question3)
    option3 = ["1.elephant", "2.tiger", "3.Lion", "4.monkey"]
    print(option3)
    correct_answer3 = int(
        input("enter your answer's option as per the rule\n"))
    if correct_answer3 == 3:
      print("CONGRATULATION YOU HAVE SELECTED CORRECT OPTION")
      print("you have won 30 lakhs!!!!!!!!!!!!!!!")
      print("get ready for the next question")
      print("\n")
      #-----------------question 4 workplace---------------
      question4 = ["who is the current presedent of INDIA?"]
      print(question4)
      option4 = [
          "1.rahul gandhi", "2.narendra modi", "3.Drupadhi murmu",
          "4.none of above"
      ]
      print(option4)
      correct_answer4 = int(
          input("enter your answer's option as per the rule\n"))
      if correct_answer4 == 3:
        print("CONGRATULATION YOU HAVE SELECTED CORRECT OPTION")
        print("you have won 40 lakhs!!!!!!!!!!!!!!!")
        print("get ready for the next question")
        print("\n")
        #-----------------question 5 workplace---------------
        question5 = [
            "how many planets we got in our solar system?(including pluto)"
        ]
        print(question5)
        option5 = [6, 8, 9, 5]
        print(option5)
        correct_answer5 = int(
            input("enter your answer's option as per the rule\n"))
        if correct_answer5 == 3:
          print("CONGRATULATION YOU HAVE SELECTED CORRECT OPTION")
          print("you have won 50 lakhs!!!!!!!!!!!!!!!")
          print("get ready for the next question")
          print("\n")
          #-----------------question 6 workplace---------------
          question6 = ["Portugal is in which continent?"]
          print(question6)
          option6 = ["1.Europe", "2.Asia", "3.Africa", "4.North America"]
          print(option6)
          correct_answer6 = int(
              input("enter your answer's option as per the rule\n"))
          if correct_answer6 == 1:
            print("CONGRATULATION YOU HAVE SELECTED CORRECT OPTION")
            print("you have won 60 lakhs!!!!!!!!!!!!!!!")
            print("get ready for the next question")
            print("\n")
            #-----------------question 7 workplace---------------
            question7 = ["after which god/godesses Mumbai had named?"]
            print(question7)
            option7 = ["1.Ganesha", "2.Maha Dev", "3.Shiva", "4.Mumba Devi"]
            print(option7)
            correct_answer7 = int(
                input("enter your answer's option as per the rule\n"))
            if correct_answer7 == 4:
              print("CONGRATULATION YOU HAVE SELECTED CORRECT OPTION")
              print("you have won 70 lakhs!!!!!!!!!!!!!!!")
              print("get ready for the next question")
              print("\n")
              #-----------------question 8 workplace---------------
              question8 = ["who was the first male india to go to space"]
              print(question8)
              option8 = [
                  "1.Kalpna Chavla", "2.Rakesh Sharma", "3.Nile Armstrong",
                  "4.None"
              ]
              print(option8)
              correct_answer8 = int(
                  input("enter your answer's option as per the rule\n"))
              if correct_answer8 == 2:
                print("CONGRATULATION YOU HAVE SELECTED CORRECT OPTION")
                print("you have won 80 lakhs!!!!!!!!!!!!!!!")
                print("get ready for the next question")
                print("\n")
                #-----------------question 9 workplace---------------
                question9 = ["who was the first FIFA mens tournament winner"]
                print(question9)
                option9 = ["1.Argentina", "2.Brazil", "3.Uruguay", "4.France"]
                print(option9)
                correct_answer9 = int(
                    input("enter your answer's option as per the rule\n"))
                if correct_answer9 == 3:
                  print("CONGRATULATION YOU HAVE SELECTED CORRECT OPTION")
                  print("you have won 90 lakhs!!!!!!!!!!!!!!!")
                  print("get ready for the next question")
                  print("\n")
                  #-----------------question 10 workplace---------------
                  question10 = ["who you should love and repect more?"]
                  print(question10)
                  option10 = [
                      "1.yourself", "2.your family", "3.your friends", "4.noe"
                  ]
                  print(option10)
                  correct_answer10 = int(
                      input("enter your answer's option as per rule\n"))
                  if correct_answer10 == 2:
                    print("CONGRATULATION YOU HAVE SELECTED CORRECT OPTION")
                    print("you have won 1 crore!!!!!!!!!!!!!!!")
                    print("HOPE you like NRG's KBC")
                    print("THANK YOU FOR PLAYING")
                    print("\n")
                  else:
                    print("Close but not SIGAR")
                    print(
                        "sorry to say you have to leave the game but you won 90 Laks"
                    )

                else:
                  print("soory you have selected wrong answer")
                  print(
                      "sorry but you have to leave the game but you won 80 Laks"
                  )
              else:
                print("sorry you have selected wrong answer")
                print(
                    "sorry to say but you have to leave the game but you won 70 Laks"
                )
            else:
              print("sorry you have selected wrong answer")
              print(
                  "sorry to say but you have to leave the game but you  won 60 Laks"
              )
          else:
            print("sorry you have selected wrong answer")
            print(
                "sorry to say but you have to leave the game but yoy have won 50 Laks"
            )
        else:
          print("sorry you have selected wrong answer")
          print(
              "sorry to say but you have to leave the game but yoy have won 40 Laks"
          )
      else:
        print("sorry you have selected wrong answer")
        print(
            "sorry to say but you have to leave the game but yoy have won 30 Laks"
        )

    else:
      print("sorry you have selected wrong answer")
      print(
          "sorry to say but you have to leave the game but yoy have won 20 Laks"
      )
  else:
    print("sorry you have selected wrong answer")
    print(
        "soory to say but you have to leave the game but you have won 10 lakhs"
    )

# ------------------------question 1 workplace------------------

