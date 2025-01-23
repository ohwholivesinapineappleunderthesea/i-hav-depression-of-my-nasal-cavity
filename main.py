quiz_questions = [
    "what is yahya's favorite food?",
    "what is the capital of nigeria?",
    "what is the largest land animal?",
    "who wrote the song 'Im fat' ?"
]

quiz_answers = [
    "halal meats",
    "not defined",
    "yahya",
    "weird Al"
]

score = 0

for question in quiz_questions:
    print(f"Question: {question}\n")

PA1 = input("what is Q1: ")
if PA1 == "halal meats":
    score += 1
else:
    print("yeah no thats wrong you suck the answer is halal meats")

PA2 = input("what is Q2: ")
if PA2 == "not defined":
    score += 1
else:
    print("ok man what i tell you, i dont even know")

PA3 = input("what is Q3: ")
if PA3 == "yahya":
    score += 6
else:
    print("BUDDY ARE YOU DUMB ITS YAHYA")

PA4 = input("what is Q4: ")
if PA4 == "weird Al":
    score += 2
else:
    print ("werid Al man, wierd Al")


print (f"your final score is: {score} /10")
        
    

