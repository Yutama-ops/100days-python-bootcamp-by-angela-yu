from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
# question data is a dictionary containing a
# question and answer list
# and here we put the dictionary in a list called
# a question_bank
for question in question_data:
    new_question = Question(question["question"], question["correct_answer"])
    question_bank.append(new_question)

# creating an object called quiz and storing the data
# of the question_bank to the format of Quiz brain
quiz = QuizBrain(question_bank)

while quiz.still_have_question():
    print(quiz.next_question())

print("You've completed the quiz")
print(f"Your final score was : {quiz.score}/12")
