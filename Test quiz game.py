while True:
    score = 0
    print("Welcome to my computer quiz!")

    playing = input("Do you want to play?: ")

    if playing.lower() != "yes":
        exit()

    print("Okay!, Let's play :D")

    # Question 1
    answer = int(input("What is the sum of 8 + 9?: "))
    if answer == 17:
        print("Correct!")
        score += 1
    else:
        print("Incorrect :C")
        

    # Question 2
    answer2 = input("What does this anagram mean? YAILT: ")
    if answer2.lower() != "italy":
        print("Incorrect!")
        
    else:
        print("Good job!")
        score += 1

    # Question 3
    answer3 = input("What is the capital of France?: ")
    if answer3.lower() != "paris":
        print("Incorrect!")
        
    else:
        print("Superb!")
        score += 1

    # Question 4
    answer4 = float(input("What is 5/10?: "))
    if answer4 == 0.5:
        print("Perfect!")
        score += 1
    else:
        print("Incorrect!")
        
    print("That's all the questions")
    print(f"You got {score} out of 4 questions correct!")

    # Play again
    play_again = input("Do you want to play again? ").lower()
    if play_again != "yes":
        print("Goodbye, hope you had a good time!")
        break
