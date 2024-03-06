from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    current_question = Question(question["text"], question["answer"])
    # print(current_question)
    question_bank.append(current_question)

this_brain = QuizBrain(question_bank)

while this_brain.still_has_question():
    this_brain.next_question()
    print(this_brain.score)
