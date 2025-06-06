from tabnanny import check


class QuizBrain:
    def __init__(self, q_list):
        self.question_num = 0
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self) :
        return self.question_num < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_num]
        self.question_num += 1
        user_answer = input(f"Q.{self.question_num} : {current_question.text}  (True / False) : ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower() :
            print("The answer is correct")
            self.score += 1
        else :
            print("Oops! Wrong answer")
        print(f"Your score is {self.score}/{self.question_num} \n")