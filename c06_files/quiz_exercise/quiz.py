"""
sample `questions.txt` file:
1+1=2
2+2=4
8-4=4
task description:
- read from `questions.txt`
- for each question, print out the question and and wait for the user's answer
    for example, for the first question, print out: `1+1=`
- after the user answers all the questions, calculate her score and write it to the `result.txt` file
    the result should be in such format: `Your final score is n/m.`
    where n and m are the number of correct answers and the maximum score respectively
"""

quiz = open('questions.txt','r')
questions = [line.strip() for line in quiz.readlines()]
quiz.close()

print(questions)

results = [0,0]

for question in questions:
    student_answer = input(question[0:question.index('=')+1])
    answer = question[question.index('=')+1:]
    if answer == student_answer:
        results[0] += 1
    else:
        results[1] += 1

score = results[0]/(results[0]+results[1])

results_file = open('result.txt','w')

results_file.write(f'Your final score is {results[0]}/{results[0]+results[1]}.')

results_file.close()





