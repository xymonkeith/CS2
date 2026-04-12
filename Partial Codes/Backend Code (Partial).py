def RunIntelligenceQuiz():
    
    def Quiz1():
        #Linguistic Intelligence
    
    def Quiz2():
        #Logical-Mathematical Intelligence

    def Quiz3():
        #Spatial Intelligence

    def Quiz4():
        #Interpersonal Intelligence
    
    def Quiz5():
        #Intrapersonal Intelligence

    def Quiz6():
        #Naturalistic Intelligence
    
    return score


def PBC_Calculator():
    




def Quiz(): # function to start flow of program
    QuizType = 1       # track the type of quiz

    print("Welcome to Puzzling Out Intelligence")

    # M E N U_
    while True:
        StartQuiz = input("Start Quiz? (Y/N): ").strip().upper()

        if StartQuiz == "Y":
            break

        elif StartQuiz == "N":
            while True:
                ExitQuiz = input("Do you want to quit? (Y/N): ").strip().upper()

                if ExitQuiz == "Y":
                    print("Goodbye!")
                    exit()
                elif ExitQuiz == "N":
                    print("Returning to start menu...")
                    break
                else:
                    print("Invalid input. Enter Y or N.")

        else:
            print("Invalid input. Enter Y or N.")
    # M E N U

    
    
    


    # R U N     Q U I Z 
    print("Beginning quiz, goodluck.")
    quiz_functions = [Quiz1, Quiz2, Quiz3, Quiz4, Quiz5, Quiz6] # quiz types that will run

    for quiz_func in quiz_functions:
        quiz_func()  # runs each quiz in order

    # R U N     Q U I Z

    
    # calculate score
    print("Quiz done. Calculating score...")
        


Quiz()


