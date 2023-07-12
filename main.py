from question_model import Question
from data import trivia_question_data
from quiz_brain import QuizBrain

question_bank = []

for q_data in trivia_question_data:
    new_question = Question(q_data["question"], q_data["correct_answer"])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")
