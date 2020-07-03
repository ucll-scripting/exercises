import csv

with open('solutions.csv') as file:
    solutions = file.read().strip().split(',')

with open('answers.csv') as file:
    reader = csv.reader(file)
    for student, *answers in reader:
        score = sum( 1 for solution, answer in zip(solutions, answers) if solution == answer )
        print(f'{student} {score}')