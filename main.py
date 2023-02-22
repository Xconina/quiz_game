# create a model for a question in the quiz
# attributes, text , answer. init with value when new q object is created
# ex. new_q = Question("2+2=4", "True") -- now the new q has been created with the text and answer init
import random
from data import question_banks

from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
question_data = random.choice(question_banks)

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
print(f"You have completed the quiz! Your final score was {quiz.score}/{len(question_bank)}.")
