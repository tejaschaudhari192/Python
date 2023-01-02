from data import question_data
from question_model import qn
from quiz_brain import Qz

QnBank = []

for i in question_data:
    qd = qn(i["text"], i["answer"])
    QnBank.append(qd)

# print(QnBank)
quiz = Qz(QnBank)

while quiz.quiz_continue():
    quiz.next()

print('Quiz Completed !')
print(f'Final Score {quiz.score}/{quiz.nofqns}')

# for i in question_data:
#     qsn = i["text"]
#     ans=i["answer"]
#     qd = qn(qsn,ans)
#     QnBank.append(qd)