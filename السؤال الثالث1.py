

import random
def quiz():
    score=0
    questionsRight=0
    fileName='f:\\ph.csv'
    quizFile = open(fileName,"r")
    quizData = quizFile.readlines()
    random.shuffle(quizData)
    questionno=1
    for i in range(20):
        x = quizData[i].strip()
        data = x.split(",")        
        question = data[0]
        CorrectAnswer = data[1]

        print("Question #",questionno)
        print(question)
        answer = input("What is your answer? ")
        if answer == CorrectAnswer:
            print("Correct!")
            score=score+1
            questionsRight=questionsRight+1
            questionno = questionno+1

        else:
            print("Incorrect.")
            print("Correc answer should be: "+CorrectAnswer)
            questionno = questionno+1
        print()

    totalScore = (score / 10) * 100
    print("You got ",score," questions right, and a score of ",totalScore,"%.")
quiz()
