# -*- coding: utf-8 -*-
"""
Created on Thu May 23 18:37:13 2024

@author: zohai
"""

questions = [           #array for questions the quiz will ask in the function being defined 
    {
     "prompt": "What is the capital of Pakistan?",
     "options": ["A. Lahore", "B. Burewala", "C. Islamabad", "D. Karachi"],
     "answer": "C"
     },
    {
     "prompt": "Which language is primarily spoken in Pakistan?",
     "options": ["A. Urdu", "B. Punjabi", "C. Arabic", "D. Hindi"],
     "answer": "A"
     },
    {
     "prompt": "How many countries are there in the world?",
     "options": ["A. 183", "B. 206", "C. 217", "D. 195"],
     "answer": "D"
     },
    {"prompt": "Who wrote the Percy Jackson series?",
     "options": ["A. J.K. Rowling", "B. Rick Riordan", "C. Tareef Sharieff", "D. Suzanne Collins"],
     "answer": "B"
     },
    ]

def run_quiz(questions):
    score = 0
    for question in questions: #going to go through each question from the top
        print(question["prompt"])
        for option in question["options"]: #to list options
            print(option)
        answer = input("Enter your answer (A. B. C. D): ").upper() #if answer is lowercase itll still apply as uppercase
        if answer == question["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print("Incorrect! The correct answer was", question["answer"], "\n")
            
    print(f"You got {score} out of {len(questions)} questions correct.") #f string allows you to plug in variables instead of string print function with squigly brackets 
    
run_quiz(questions)