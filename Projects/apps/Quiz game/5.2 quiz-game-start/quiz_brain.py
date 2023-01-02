class Qz:
    def __init__(self, qb):
        self.q_num = 0
        self.score = 0
        self.q_list = qb
        self.nofqns = len(qb)

    def quiz_continue(self):
        if len(self.q_list) <= self.q_num:
            return False
        else:
            return True

    def next(self):
        currentqn = self.q_list[self.q_num]
        print('Whats in current :', currentqn)
        self.q_num += 1
        user_ans = input(
            f'Q.{self.q_num} : {currentqn.txt} (True/False)? : ').lower()
        self.check(currentqn.ans.lower(), user_ans.lower())

    def check(self, right_ans, user_ans):
        if right_ans == user_ans:
            print(f'Correct ans')
            self.score += 1

        else:
            print(f'Wrong ans')
        print(f'Ans : {right_ans}')
        print(f'Score {self.score}/{self.q_num} \n\n')
