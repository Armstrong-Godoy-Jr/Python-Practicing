# Constructing the dictionary and receiving the values

student = dict()
student['Name'] = str(input('Type your name: '))
student['Average'] = float(input(f'Average score of {student["Name"]}: '))

# Status (Pass or Fail):

if student['Average'] >= 7:
    student['Situation'] = 'Pass'
    print('Congratulations!')
elif student['Average'] < 7:
    student['Situation'] = 'Fail'
    print('Study more in the next time!')
print('+--' * 10)

# Showing contents of the dictionary

for k, v in student.items():
    print(f'{k} is {v}.')