class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        q_text = self.question_list[self.question_number].text
        answer = input(f"Q.{self.question_number + 1} {q_text} (True/False): ")
        if self.check_answer(answer):
            print("Great!!")
            self.score += 1
        else:
            print("Bad!!")

        self.question_number += 1

    def still_has_question(self):
        if self.question_number >= len(self.question_list):
            return False
        return True

    def check_answer(self, answer):
        if answer == self.question_list[self.question_number].answer:
            return True
        return False
